from playwright.sync_api import Page, expect, TimeoutError
import pytest
import re

def test_dynamicID(page: Page):
    # Record button click.
    # Then execute your test to make sure that ID is not used for button identification
    
    page.goto("http://uitestingplayground.com/dynamicid")
        
    button = page.get_by_role("button", name="Button with Dynamic ID")
    button.click()

    expect(button).to_be_visible


def test_class_attribute(page: Page):
    # Record primary (blue) button click and press ok in alert popup.
    # Then execute your test to make sure that it can identify the button using btn-primary class.
    
    page.goto("http://uitestingplayground.com/classattr")

    primary_btn = page.locator("button.btn-primary")

    expect(primary_btn).to_be_visible
    primary_btn.click()


def test_hidden_layers(page: Page):
    # Record button click and then duplicate the button click step in your test.
    # Execute the test to make sure that green button can not be hit twice.
    
    page.goto("http://uitestingplayground.com/hiddenlayers")

    green_btn = page.locator("button#greenButton")
    green_btn.click()
    expect(green_btn).to_be_disabled


def test_load_delay(page: Page):
    # Navigate to Home page and record Load Delays link click and button click on this page.
    # Then play the test. It should wait until page is loaded.
    
    page.goto("http://uitestingplayground.com/home")
    
    load_delay_link = page.get_by_role("link", name="Load Delay")
    load_delay_link.click()

    button = page.get_by_role("button",name="Button Appearing After Delay")
    button.click()

    expect(button).to_be_visible


def test_ajax_data(page: Page):
    # Record the following steps. Press the button below and wait for data to appear (15 seconds), 
    # click on text of the loaded label.
    # Then execute your test to make sure it waits for label text to appear.

    page.goto("http://uitestingplayground.com/ajax")
    button = page.get_by_role("button", name="Button Triggering AJAX Request")
    button.click()

    ajax_data = page.locator("p.bg-success")
    ajax_data.wait_for()

    expect(ajax_data).to_be_visible()
    

def test_click(page: Page):
    # Record button click. The button becomes green after clicking.
    # Then execute your test to make sure that it is able to click the button.
    
    page.goto("http://uitestingplayground.com/click")
    
    button = page.locator("button.btn-primary")
    button.click()
    expect(button).to_have_class("btn btn-success")


def test_text_input(page: Page):
    # Record setting text into the input field and pressing the button.
    # Then execute your test to make sure that the button name is changing.
    
    page.goto("http://uitestingplayground.com/textinput")

    text = "test input"
    input = page.get_by_placeholder("MyButton")
    input.fill(text)
    
    button = page.locator("button.btn-primary")
    button.click()

    expect(button).to_have_text(text)


def test_scrollbar(page: Page):
    # Find a button in the scroll view and record button click.
    # Update your test to automatically scroll the button into a visible area.
    # Then execute your test to make sure it works.

    page.goto("http://uitestingplayground.com/scrollbars")

    button = page.locator("button.btn-primary")
    button.scroll_into_view_if_needed() # button.click() also works since playwright does auto-scroll

    expect(button).to_be_in_viewport

def test_dynamic_table(page: Page):
    # For Chrome process get value of CPU load.
    # Compare it with value in the yellow label.
    page.goto("http://uitestingplayground.com/dynamictable")
    
    headers = page.get_by_role("columnheader")
    cpu_col = None

    for i in range(headers.count()):
        if headers.nth(i).inner_text() == "CPU":
            cpu_col = i
            break
    
    rowgroup = page.get_by_role("rowgroup").last
    row = rowgroup.get_by_role("row").filter(has_text="Chrome")
    chrome_cpu = row.get_by_role("cell").nth(cpu_col)

    label = page.locator("p.bg-warning").inner_text()
    text_percentage = label.split()[-1]

    expect(chrome_cpu).to_have_text(text_percentage)


def test_verify_text(page: Page):
    # Create a test that finds an element with Welcome... text.
    
    page.goto("http://uitestingplayground.com/verifytext")

    welcome_text = page.locator("div.bg-primary").get_by_text("Welcome")
    expect(welcome_text).to_contain_text("Welcome")


def test_progress_bar(page: Page):
    # Create a test that clicks Start button and then waits for the progress bar to reach 75%. 
    # Then the test should click Stop. 
    # The less the differnce between value of the stopped progress bar and 75% the better your result.

    page.goto("http://uitestingplayground.com/progressbar")

    start_btn = page.get_by_role("button", name="Start")
    stop_btn = page.get_by_role("button", name="Stop")
    progress_bar = page.locator("div.bg-info")

    start_btn.click()
    
    while True:
        valuenow = int(progress_bar.get_attribute("aria-valuenow"))
        if valuenow >= 30:
            stop_btn.click()
            break

    # expect().to_be_greater_than_or_equal() has compatibility issue on current python version
    assert valuenow >= 75


def test_visibility(page: Page):
    #Learn locators of all buttons.
    #In your testing scenario press Hide button.
    #Determine if other buttons visible or not.

    page.goto("http://uitestingplayground.com/visibility")

    btn_hide = page.get_by_role("button", name="Hide")
    btn_removed = page.get_by_role("button", name="Removed")
    btn_zero_width = page.get_by_role("button", name="Zero Width")
    btn_overlapped = page.get_by_role("button", name="Overlapped")
    btn_opacity = page.get_by_role("button", name="Opacity 0")
    btn_hidden = page.get_by_role("button", name="Visibility Hidden")
    btn_none = page.get_by_role("button", name="Display None")
    btn_offscreen = page.get_by_role("button", name="Offscreen")

    btn_hide.click()

    expect(btn_removed).to_be_hidden()
    expect(btn_zero_width).to_have_css("width", "0px")
    with pytest.raises(TimeoutError):
        btn_overlapped.click(timeout=2000)
    expect(btn_opacity).to_have_css("opacity", "0")
    expect(btn_hidden).to_be_hidden()
    expect(btn_none).to_be_hidden()
    expect(btn_offscreen).not_to_be_in_viewport()


def test_login(page: Page):
    # Fill in and submit the form. For successfull login use any non-empty user name and `pwd` as password.

    page.goto("http://uitestingplayground.com/sampleapp")

    input_username = page.get_by_placeholder("User Name")
    input_password = page.get_by_placeholder("********")
    btn_login = page.get_by_role("button", name="Log In")
    message = page.locator("label.text-success")

    username = "Test Username"
    password = "pwd"
    input_username.fill(username)
    input_password.fill(password)
    btn_login.click()

    expect(message).to_have_text(f"Welcome, {username}!")

def test_mouseover(page: Page):
    # Record 2 consecutive link clicks.
    # Execute the test and make sure that click count is increasing by 2.

    page.goto("http://uitestingplayground.com/mouseover")

    link = page.get_by_title("Click me")
    link.hover()
    
    active_link = page.get_by_title("Active link")
    active_link.click(click_count=2)
    click_count = page.locator('span#clickCount')

    expect(click_count).to_have_text("2")


def test_nbsp(page: Page):
    # Use the following xpath to find the button in your test:
    # //button[text()='My Button']
    # Notice that the XPath does not work. 
    # Change the space between 'My' and 'Button' to a non-breaking space. 
    # This time the XPath should be valid.

    page.goto("http://uitestingplayground.com/mouseover")

    button = page.locator("//button[text()='My\u00a0Button]")
    button.click(timeout=2000)

    expect(button).to_be_enabled


def test_overlapped(page: Page):
    # Record setting text into the Name input field (scroll element before entering the text).
    # Then execute your test to make sure that the text was entered correctly.

    page.goto("http://uitestingplayground.com/overlapped")

    name_field = page.get_by_placeholder("Name")

    div = name_field.locator("..")
    div.hover()

    page.mouse.wheel(0, 200)

    value_input = "testing"
    name_field.fill(value_input)

    expect(name_field).to_have_value(value_input)


