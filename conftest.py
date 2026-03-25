import pytest
import os


def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Serial</th>")
    cells.insert(3, "<th>PO</th>")


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{getattr(report, 'serial', '')}</td>")
    cells.insert(3, f"<td>{getattr(report, 'po', '')}</td>")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        # ✅ attach dynamic data
        report.serial = getattr(pytest, "serial", "")
        report.po = getattr(pytest, "po", "")

        # ✅ attach steps into LOG (this fixes your issue)
        steps = getattr(pytest, "steps", [])

        if steps:
            report.sections.append(("Steps", "\n".join(steps)))

        # ✅ screenshot on failure
        if report.failed:
            page = item.funcargs.get("page", None)
            if page:
                os.makedirs("reports/screenshots", exist_ok=True)
                file_path = f"reports/screenshots/{item.name}.png"
                page.screenshot(path=file_path)