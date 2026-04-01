from playwright.sync_api import sync_playwright
import pytest
import datetime
from pathlib import Path

# create fixture
@pytest.fixture(autouse=True, scope="session") 
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    
    # create context and trace
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = context.new_page()
    
    yield page
    
    # teardown: test finished and save trace with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # create traces dir if not exist
    trace_dir = Path("traces")
    trace_dir.mkdir(exist_ok=True)

    trace_path = trace_dir / f"trace_{timestamp}.zip"
    
    context.tracing.stop(path=trace_path)
    print(f"Trace saved to:{trace_path}")
    
    context.close()
    browser.close()
    playwright.stop()