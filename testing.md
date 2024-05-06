## Test Case: User Registration - Email Validation
**Expected:** User registration should fail if an invalid email address is provided.

**Testing:** Attempted to register with an email address lacking the "@" symbol.

**Result:** Registration form submitted successfully despite invalid email format.
### Steps Taken:
* Reviewed the email validation regex pattern used in the registration form.
* Identified that the regex pattern did not account for the "@" symbol.
* Updated the email validation regex pattern to ensure it includes the "@" symbol.
* Retested user registration with an invalid email format.
* Verification: Registration failed as expected when an invalid email format was provided.

## Test Case: User Registration - Password Strength Requirement
**Expected:** User should be prompted to choose a stronger password if the entered password is weak.

**Testing:** Attempted to register with a password that did not meet the minimum strength requirements.

**Result:** Registration form accepted the weak password without prompting for a stronger one.
### Steps Taken:
* Reviewed the password strength validation function used in the registration process.
* Identified that the function did not enforce the minimum strength requirements.
* Updated the password strength validation function to include checks for minimum length and complexity.
* Retested user registration with a weak password.
* Verification: Registration failed as expected, prompting the user to choose a stronger password.

## Test Case: Email Sending - Order Confirmation
**Expected:** Order confirmation email should be sent to the user upon successful checkout.

**Testing:** Completed a successful checkout process with valid shipping information.

**Result:** No order confirmation email received after completing the checkout process.
### Steps Taken:
* Reviewed the email sending function used in the checkout process.
* Identified that the function was not being called after a successful checkout.
* Updated the checkout view to invoke the email sending function upon successful order creation.
* Retested the checkout process and completed a successful purchase.
* Verified the email inbox for the order confirmation email.
* Verification: Order confirmation email received in the inbox after successful checkout.

## Test Case: Password Reset - Email Request
**Expected:** User should receive an email with instructions for resetting the password upon request.

**Testing:** Requested a password reset by entering the registered email address.

**Result:** Password reset email received promptly with instructions.
### Steps Taken:
* Accessed the "Forgot Password" page and entered the registered email address.
* Submitted the password reset request.
* Checked the email inbox for the password reset email.
* Opened the email and followed the instructions to reset the password.
* Verification: Received the password reset email and successfully reset the password.

## Test Case: User Profile Update - Email Change
**Expected:** User's email address should be updated successfully after submitting a request.

**Testing:** Updated the email address in the user profile settings.

**Result:** Email address updated successfully, and confirmation email received.
### Steps Taken:
* Accessed the user profile settings page.
* Edited the email address field and submitted the changes.
* Checked the inbox for the email associated with the email change request.
* Opened the confirmation email and clicked on the verification link.
* Verification: Email address updated in the user profile settings.

## Test Case: Product Search - Keyword Matching
**Expected:** Search functionality should return relevant products based on the entered keywords.

**Testing:** Entered specific keywords related to a product in the search bar.

**Result:** Search results displayed relevant products matching the entered keywords.
### Steps Taken:
* Accessed the search bar on the homepage.
* Entered specific keywords related to a product (e.g., "frying pan").
* Submitted the search query and reviewed the search results.
* Verified that the displayed products matched the entered keywords.
* Verification: Found relevant products matching the entered keywords in the search results.

## Test Case: Category Selection - Navigation
**Expected:** Clicking on a category should navigate to a page displaying products within that category.

**Testing:** Clicked on a specific category in the navigation menu.

**Result:** Redirected to a page displaying products belonging to the selected category.
### Steps Taken:
* Accessed the navigation menu containing different product categories.
* Clicked on a specific category, such as "Electronics".
* Verified that the page displayed products exclusively from the selected category.
* Verification: Successfully navigated to the category-specific page showing relevant products.

## Test Case: Database Integrity - Product Deletion
**Expected:** Deleting a product should remove it from the database without affecting other data.

**Testing:** Deleted a product entry from the database.

**Result:** The product was successfully removed from the database, and associated data remained intact.
### Steps Taken:
* Accessed the admin panel to locate the product to be deleted.
* Selected the product and initiated the deletion process.
* Confirmed the deletion action and reviewed the database to ensure the product was removed.
* Verified that other related data, such as orders or reviews, remained unaffected.
* Verification: Observed the product's absence in the database and verified the integrity of associated data.

## Test Case: Category Creation - Database Update
**Expected:** Creating a new category should update the database with the new category information.

**Testing:** Added a new category through the admin panel.

**Result:** The new category was successfully added to the database, and it appeared in the category list.
### Steps Taken:
* Accessed the admin panel and navigated to the category management section.
* Initiated the creation of a new category by providing the required details.
* Saved the changes and confirmed the addition of the new category.
* Reviewed the database to ensure the new category entry was recorded.
* Verification: Found the new category entry in the database, confirming successful creation and database update.

## Test Case: Add Product - Staff Access
**Expected:** Staff members should be able to access the product addition functionality.

**Testing:** Logged in as a staff member and accessed the product addition page.

**Result:** Successfully accessed the product addition page with staff credentials.
### Steps Taken:
* Logged into the system using staff credentials.
* Navigated to the product addition page.
* Verified that the staff member could view and interact with the product addition form.
* Attempted to submit a new product entry.
* Verification: Successfully added a new product, confirming staff access to product addition functionality.

## Test Case: Edit Blog Entry - Staff Authorization
**Expected:** Staff members should have the authority to edit existing blog entries.

**Testing:** Logged in as a staff member and attempted to edit a blog entry.

**Result:** Able to access and modify the content of an existing blog entry.
### Steps Taken:
* Logged into the system using staff credentials.
* Accessed the list of existing blog entries.
* Selected a blog entry to edit and initiated the editing process.
* Made necessary changes to the blog content and saved the modifications.
* Verified that the changes were reflected in the updated blog entry.
* Verification: Observed the updated content in the edited blog entry, confirming staff authorization for blog editing.

## Test Case: View Contact Form Messages - Staff Access
**Expected:** Staff members should have access to view messages submitted through the contact form.

**Testing:** Logged in as a staff member and navigated to the contact form messages section.

**Result:** Able to view and review messages submitted through the contact form.
### Steps Taken:
* Logged into the system using staff credentials.
* Accessed the section containing messages submitted through the contact form.
* Reviewed the list of messages, including sender details and message content.
* Opened individual messages to read their contents and review sender information.
* Verification: Confirmed staff access to contact form messages and ability to view message details.

## Test Case: Add Blog Entry - Staff Privilege
**Expected:** Staff members should possess the privilege to add new blog entries.

**Testing:** Logged in as a staff member and attempted to create a new blog entry.

**Result:** Successfully accessed the blog creation form and submitted a new blog entry.
### Steps Taken:
* Logged into the system using staff credentials.
* Accessed the blog creation page to initiate the process of adding a new blog entry.
* Provided relevant details, including title, content, and publication date, in the blog creation form.
* Saved the new blog entry and confirmed its addition to the system.
* Verified that the newly added blog entry appeared in the list of blog posts.
* Verification: Observed the presence of the newly added blog entry, confirming staff privilege to create blog posts.

### Test Case: Login Button Functionality
**Expected:** Clicking the login button should submit the login form and authenticate the user.

**Testing:** Clicked on the login button after entering valid login credentials.

**Result:** User successfully logged in and redirected to the dashboard page.
#### Steps Taken:
- Entered valid username and password in the login form.
- Clicked on the login button.
- Observed successful authentication message and redirection to the dashboard.
- *Verification:* Logged-in user's name displayed in the header, confirming successful login.

**Expected:** Clicking the login button without entering any credentials should display an error message.

**Testing:** Clicked on the login button without entering any username or password.

**Result:** Received an error message prompting to enter valid login credentials.
#### Steps Taken:
- Left both username and password fields empty.
- Clicked on the login button.
- Observed error message indicating that login credentials are required.
- *Verification:* Confirmed error message displayed as expected when no credentials were provided.

### Test Case: Navigation Links
**Expected:** Clicking on a navigation link should redirect the user to the corresponding page.

**Testing:** Clicked on the "Home" navigation link.

**Result:** Successfully redirected to the home page.
#### Steps Taken:
- Located and clicked on the "Home" navigation link.
- Observed redirection to the home page.
- Verified that the content of the home page was displayed.
- *Verification:* Confirmed successful navigation to the home page.

**Expected:** Clicking on a disabled navigation link should not trigger any action.

**Testing:** Attempted to click on a disabled "Admin Dashboard" navigation link.

**Result:** No response or redirection occurred upon clicking the disabled link.
#### Steps Taken:
- Identified and clicked on the "Create Blog Post" navigation link, which was disabled.
- Observed a redirect to the homepage for non-staff users.
- Verified that the disabled link remained inactive.
- *Verification:* Confirmed that clicking on the disabled link did not produce any action, as expected.

### Test Case: Product Price Validation
**Expected:** Users should not be able to add products with negative prices.

**Testing:** Attempted to add a product with a negative price (-€10).

**Result:** The product was successfully added despite the negative price.
#### Steps Taken:
- Reviewed the product creation form and associated validation logic.
- Identified that the validation did not include a check for negative prices.
- Updated the product creation form validation to include a check for negative prices.
- Retested product addition with a negative price.
- *Verification:* Confirmed that the product addition failed with an error message for negative prices.

### Test Case: Product Price Field Validation
**Expected:** The product creation form should display an error message when a negative price is entered.

**Testing:** Entered a negative price (-€5) in the price field of the product creation form.

**Result:** The form accepted the negative price without displaying any validation error.
#### Steps Taken:
- Reviewed the frontend validation scripts associated with the product creation form.
- Found that the frontend validation did not include a check for negative prices.
- Updated the frontend validation scripts to include validation for negative prices.
- Retested the product creation form with a negative price.
- *Verification:* Confirmed that the form displayed an error message for negative prices.

### Test Case: Product Price Update Validation
**Expected:** Users should not be able to update product prices to negative values.

**Testing:** Attempted to update a product's price to a negative value (-€15).

**Result:** The product price was successfully updated to the negative value.
#### Steps Taken:
- Reviewed the product update form and associated validation logic.
- Discovered that the validation for product updates did not include a check for negative prices.
- Updated the product update form validation to include a check for negative prices.
- Retested product price updates with a negative value.
- *Verification:* Confirmed that the product price update failed with an error message for negative prices.
