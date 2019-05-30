# python-selenium-chrome-html-to-pdf-converter
Simple python wrapper to convert HTML to PDF with headless Chrome via selenium

## Installation
Clone repository, move to project root dir, install virtualenv, install dependencies:
```
git clone https://github.com/maxvst/python-selenium-chrome-html-to-pdf-converter.git
cd python-selenium-chrome-html-to-pdf-converter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Install chrome (chromium) browser.
Download chromedriver from http://chromedriver.chromium.org/ and put it project root directory

## Demo
```
cd examples
python converter.py https://google.com google.pdf
```

## Why use selenium?
TODO: Add description

## CSS recomendations

Set page size.
```
@page {
	size: A4;  /* see https://developer.mozilla.org/en-US/docs/Web/CSS/@page/size */
}
```
See https://developer.mozilla.org/en-US/docs/Web/CSS/@page/size for more details.

## Usefull notes
See https://www.tutorialspoint.com/css/css_paged_media.htm more css properties for styling pages
