"""Change content field to JSON in JournalEntry model

Revision ID: 544595da1910
Revises: dc79a3a0a8f5
Create Date: 2024-08-28 16:22:29.580789

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '544595da1910'
down_revision = 'dc79a3a0a8f5'
branch_labels = None
depends_on = None

def upgrade():
    # Alter column 'content' in 'journal_entry' table to type JSON with an explicit cast
    with op.batch_alter_table('journal_entry', schema=None) as batch_op:
        batch_op.alter_column(
            'content',
            type_=sa.JSON(),  # SQLAlchemy JSON type
            existing_type=sa.Text(),  # Current type of 'content'
            postgresql_using='content::json'  # PostgreSQL-specific casting
        )

    # Alter column 'image_file' in 'user' table
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column(
            'image_file',
            type_=sa.String(length=20),  # New type for 'image_file'
            existing_type=sa.VARCHAR(length=255),  # Current type of 'image_file'
            existing_nullable=False
        )

    # Create new table 'journal_section' only if it doesn't exist
    if not op.get_bind().has_table('journal_section'):
        op.create_table(
            'journal_section',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('time', sa.String(length=10), nullable=False),
            sa.Column('content', sa.Text, nullable=False),
            sa.Column('image_file', sa.String(length=255), nullable=True),
            sa.Column('journal_entry_id', sa.Integer, nullable=False),
            sa.ForeignKeyConstraint(['journal_entry_id'], ['journal_entry.id']),
        )

def downgrade():
    # Drop the 'journal_section' table if it exists
    if op.get_bind().has_table('journal_section'):
        op.drop_table('journal_section')

    # Revert column 'image_file' in 'user' table
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column(
            'image_file',
            type_=sa.VARCHAR(length=255),  # Original type
            existing_type=sa.String(length=20),
            existing_nullable=False
        )

    # Revert column 'content' in 'journal_entry' table to type TEXT
    with op.batch_alter_table('journal_entry', schema=None) as batch_op:
        batch_op.alter_column(
            'content',
            type_=sa.Text(),  # Original type
            existing_type=postgresql.JSON(astext_type=sa.Text()),  # Current type of 'content'
            existing_nullable=False
        )
