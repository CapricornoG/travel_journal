# Travel Journal

## Project Overview

**Travel Journal** is a web application designed to help travellers document and share their journeys. Users can create personal accounts, log their travel experiences through journal entries, and enrich these entries with photos. The platform provides a user-friendly interface with essential features like creating, reading, updating, and deleting journal entries, along with options to make entries public or private. With built-in search and filter functionalities, users can easily find specific entries based on destinations or dates, making it an ideal tool for keeping a detailed and organised travel diary.

Key features of Travel Journal include:

- **Account Management**: Secure user registration, login, and account management.
- **Journal Management**: CRUD (Create, Read, Update, Delete) operations for journal entries with optional image uploads.
- **Search and Filtering**: Easily find journal entries by destination, date, or keywords.
- **Responsive Design**: Accessible on all devices, including mobile, tablet, and desktop, ensuring a seamless experience across platforms.

Travel Journal aims to foster a community of travel enthusiasts who can share their experiences and inspire others through their journeys. Whether for personal reflection or public sharing, the platform is tailored to make travel journaling intuitive and enjoyable.

![responsiveness](app/static/RMimages/responsive.png)


## Table of Contents
- [Travel Journal](#travel-journal)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
      - [1 - Account Management](#1---account-management)
      - [2 - Journal Management](#2---journal-management)
      - [3 - Search and Accessibility](#3---search-and-accessibility)
      - [4- User Experience](#4--user-experience)
      - [5 - Privacy and Sharing](#5---privacy-and-sharing)
    - [Site Goals](#site-goals)
      - [For New Site Users](#for-new-site-users)
      - [For Returning Site Users](#for-returning-site-users)
      - [General Goals](#general-goals)
    - [Design Choices](#design-choices)
      - [Colour Scheme](#colour-scheme)
      - [Typography](#typography)
      - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
  


## User Experience (UX)

### User Stories


####  1 - Account Management

- **As a new user, I want to create an account with a secure password and receive a confirmation, so that I can start saving my travel journal entries and personalise my experience.**

- **As a user, I want to log in and log out of my account easily, so that I can manage my sessions securely.**
- **As a returning user, I want to reset my password if I forget it, so that I can regain access to my account without issues.**
- 
#### 2 - Journal Management

- **As a user, I want to create, read, update, and delete my journal entries, so that I can keep an organised record of my travels.**
- **As a user, I want to upload photos with my journal entries, so that I can visually document my experiences.**
- **As a user, I want to add tags or categories to my journal entries, so that I can easily organise and find them later.**
  
#### 3 - Search and Accessibility

- **As a user, I want to search and filter journal entries by destination or date, so that I can quickly find specific entries.**
- **As a user, I want to view my journal entries on different devices, including mobile, tablet, and desktop, so that I can access my journals anytime, anywhere.**
  
#### 4- User Experience

- **As a first-time visitor, I want to understand the purpose of the website immediately, so that I know what value it offers me.**
- **As a user, I want clear and friendly error messages, so that I can easily understand and correct any issues I encounter.**
#### 5 - Privacy and Sharing

- **As a user, I want to set my journal entries as public or private, so that I have control over who can see my content.**
- **As a user, I want to be able to share my public journal entries with others, so that I can inspire friends or other travellers.**

### Site Goals

#### For New Site Users
- **Create a Seamless Onboarding Experience**: Ensure new users can easily understand the platform’s purpose and get started quickly with clear onboarding instructions and tutorials.
- **Simplify Account Creation**: Provide a straightforward and secure process for new users to register, including guidance on setting up their profile and starting their first journal entry.
- **Enhance Discoverability**: Make it easy for new users to explore the features of the platform and understand how to use them effectively.

#### For Returning Site Users
- **Streamline Account Management**: Offer easy-to-access options for returning users to log in, manage their account settings, and reset passwords if needed.
- **Facilitate Entry Management**: Ensure returning users can quickly create, read, update, and delete journal entries with minimal friction.
- **Provide Enhanced Search and Filtering**: Improve search and filter functionalities to help returning users find specific entries or browse through their travel history more efficiently.

#### General Goals
- **Provide a Platform for Documenting and Sharing Travel Experiences**: Allow users to create, read, update, and delete journal entries, and upload photos to enrich their entries.
- **Offer Robust Search and Filter Functionality**: Help users find journal entries by destination, date, or tags.
- **Ensure Responsiveness and User-Friendliness**: Make sure the application works seamlessly across all devices, including mobile, tablet, and desktop.


### Design Choices

#### Colour Scheme

The colour scheme has been thoughtfully crafted to evoke a sense of adventure, vibrancy, and clarity. Colours have been selected to create a cohesive palette that enhances user experience and interface aesthetics. The primary colours used are Midnight Blue for a reliable foundation, Tangerine for vibrant highlights, and Emerald Green for refreshing accents. Light Grey serves as a soft backdrop, while Dark Grey ensures clear and readable text.

- **Primary Colour**: Midnight Blue (#2C3E50) – A deep, dependable blue.
- **Secondary Colour**: Tangerine (#E67E22) – A bright, energetic orange.
- **Accent Colour**: Emerald Green (#2ECC71) – A refreshing, vibrant green.
- **Background Colour**: Light Grey (#F2F2F2) – A neutral, unobtrusive backdrop.
- **Text Colour**: Dark Grey (#333) – A strong, readable grey for text.

**Hover Effects**: 
- **Tangerine Hover**: Dark Tangerine (#D35400) – A darker shade for a more pronounced hover effect.
- **Danger Hover**: Danger Red Hover (#C0392B) – A deeper red for clear, intense hover feedback.

To create a harmonious palette, these colours were used to generate a cohesive colour scheme. You can explore and create your own colour palettes using tools such as [Coolors](https://coolors.co/).

![collours](app/static/RMimages/coolors.png)



#### Typography

The typography is designed to ensure clarity and readability while complementing the overall aesthetic of the site. The font choices are made to enhance the user experience across various elements of the application.

- **Heading Font**: Montserrat (sans-serif)
  - Used for headings (`h1`, `h2`, `h3`, `h4`, `h5`) to ensure a clean and modern look. It’s applied with varying font sizes and weights to create a clear visual hierarchy.
  - Example: `h1` is set to 3.6rem with a font-weight of 700, and `h5` is set to 2rem with text-transform: capitalize.

- **Body Font**: Merriweather (serif)
  - Chosen for body text and paragraphs for its readability and elegant serif design. It supports the main content and provides a balanced contrast to the heading font.
  - Example: Body text is set to 1.6rem with a line-height of 1.8, and special paragraphs (`.lead`) are slightly larger at 2rem with oblique styling.

- **Accent Font**: Dancing Script (cursive)
  - Used sparingly for accent elements to add a touch of personality and flair where needed.

The typography styles are applied consistently across the application to maintain a cohesive look and feel.

#### Imagery
Imagery is selected to inspire and capture the essence of travel, featuring high-quality photos of landmarks, landscapes, and cultural experiences.

- **Header Images**: Large, striking images of popular travel destinations.
- **Icons**: Simple, flat icons for navigation and action buttons.

## Wireframes
<details>
<summary>Mobile Wireframe</summary>

![Mobile View Wireframe](wireframes/mobile_wireframe.png)

</details>

## Deployment

### Local Deployment

To run this project locally, follow these steps:

1. **Clone the Repository**:
   
   Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/CapricornoG/travel_journal.git