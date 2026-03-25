import pytest
from playwright.sync_api import expect
from utils.data_generator import generate_test_data
from utils.file_generator import create_test_files
from pages.create_entry_page import CreateEntryPage
from config.config import EMAIL, PASSWORD
from faker import Faker

fake = Faker()


def test_create_entry(page):

    serial, po, desc, comments = generate_test_data()
    files = create_test_files()

    # 🔥 attach data
    pytest.serial = serial
    pytest.po = po

    # 🔥 step tracker
    pytest.steps = []
    pytest.steps.append("✔ Create Entry – PASSED")

    entry = CreateEntryPage(page)

    page.goto("https://dev.onetrace.com.au/")

    try:
        entry.login(EMAIL, PASSWORD)
        pytest.steps.append("✔ Login – PASSED")
    except:
        pytest.steps.append("❌ Login – FAILED")
        raise

    try:
        entry.create_entry_flow(serial, po, desc, comments, files["csv"])
        pytest.steps.append("✔ Create Entry – PASSED")
    except:
        pytest.steps.append("❌ Create Entry – FAILED")
        raise

    repair_comment = f"Repair-{fake.random_number(digits=5)}"

    try:
        entry.complete_repair_flow(repair_comment, files["jpg"])
        pytest.steps.append("✔ Material Received / Repair – PASSED")
    except:
        pytest.steps.append("❌ Material Received / Repair – FAILED")
        raise

    try:
        page.wait_for_timeout(5000)

    except:
        raise



  