# python-selenium-chrome-html-to-pdf-converter
Simple python wrapper to convert HTML to PDF with headless Chrome via selenium.

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

Download chromedriver from http://chromedriver.chromium.org/ and put it to project root directory.

## Demo
```
cd examples
python converter.py https://google.com google.pdf
```

## Why use selenium?
TODO: Add description

## CSS recomendations

Basic configuration for single page:
```
@page {
    size: A4;
    margin: 0mm;
}
```

For printing double-sided documents use
```
@page :left {
    margin-left: 4cm;
    margin-right: 2cm;
}

@page :right {
    margin-left: 4cm;
    margin-right: 2cm;
}

@page :first {
    margin-top: 10cm    /* Top margin on first page 10cm */
}
```

Control pagination with page-break-before, page-break-after, page-break-inside like
```
h1 { page-break-before : right }
h2 { page-break-after : avoid }
table { page-break-inside : avoid }
```
Controlling Widows and Orphans like
```
@page {
    orphans:4;
    widows:2;
}
```
