# bookmarks2maxfield

## Description

Input generator for Ingress Maxfield (http://www.ingress-maxfield.com), which
uses the export of the IITC Bookmarks Plugin as input.

## How To Use

1. Mark your portal set in IITC as bookmarks (Bookmarks Plugin).
2. Export it as file.
3. Run this script with the exported file as `<input_file>` and use the result
(standard output or content of `<output_file>`) as input for Ingress Maxfield
(http://www.ingress-maxfield.com)

## Usage

```
bookmarks2maxfield <input_file> [<output_file>]
```

### Options

```
input_file:
  IITC Bookmark Plugin export in JSON format, e.g. 'bookmarks.json'

output_file:
  generated output in CSV format, e.g. 'maxfield.csv'
```
