from pages.base_page import BasePage


class CreateEntryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def login(self, email, password):
        self.page.get_by_role("button", name="Login").click()
        self.page.get_by_role("textbox", name="Email Address").fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("checkbox", name="I accept to One Trace's Terms").check()
        self.page.get_by_role("button", name="Login").click()

        # ✅ Wait until dashboard loads
        self.page.wait_for_load_state("networkidle")

    def create_entry_flow(self, serial, po, desc, comments, file_path):

        self.page.get_by_role("button", name="Create New Entry").click()
        self.page.get_by_role("button", name="Component Repair").click()

        # ✅ Wait for form to appear
        self.page.get_by_role("textbox").nth(1).wait_for()

        # 🔥 USE CODEGEN LOCATORS (they work)
        self.page.get_by_role("textbox").nth(1).fill(serial)
        self.page.get_by_role("textbox").nth(2).fill(po)
        self.page.get_by_role("textbox").nth(3).fill(desc)

        self.page.get_by_role("textbox", name="Add Your Comments Here").fill(comments)

        self.page.get_by_text("Select Enterprise").click()
        self.page.get_by_text("Ontrace SignOff2", exact=True).click()

        self.page.get_by_role("button", name="Select File Type Dropdown").click()
        self.page.get_by_role("button", name="Purchase order").click()

        # ✅ File upload
        self.page.locator("input[type='file']").set_input_files(file_path)

        self.page.get_by_role("button", name="Submit").click()

        # ✅ Wait after submit
        self.page.wait_for_timeout(5000)

    def complete_repair_flow(self, repair_comment, file_path):

        # 🔥 Click Menu
        self.page.get_by_role("button", name="Menu").click()

        # wait for dropdown
        self.page.get_by_text("Material/Core Received").wait_for()

        # select option
        self.page.get_by_text("Material/Core Received").click()

        # confirm Yes
        self.page.get_by_role("button", name="Yes").click()

        # click Repair
        self.page.get_by_role("button", name="Repair").click()

        # wait for comments field
        comment_box = self.page.get_by_role("textbox", name="Comments *")
        comment_box.wait_for()

        # 🔥 Dynamic comment
        comment_box.fill(repair_comment)

        self.page.get_by_role("button", name="Select File Type Dropdown").click()
        self.page.get_by_role("button", name="Purchase order").click()

        # 🔥 Upload file (same way as before)
        self.page.locator("input[type='file']").set_input_files(file_path)

        # submit
        self.page.get_by_role("button", name="Submit").click()
        

        # wait for processing
        self.page.wait_for_timeout(3000)