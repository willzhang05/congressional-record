#!/usr/bin/python3
import sys
import pandas as pd
import json
from datetime import datetime
from pathlib import Path


def main():
    if (len(sys.argv) < 2):
        print("Please specify a directory for output files")
        print("Usage: ./clean.py <directory>")
        return 1
    else:
        p = Path(sys.argv[1])
        schema = {
            'doc_title': [],
            'doc_id': [],
            'turn': [],
            'speaker': [],
            'text': [],
            'speaker_bioguide': [],
            'date': []
        }

        months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']

        month_map = {month: num + 1 for num, month in enumerate(months)}

        for json_file in p.glob('**/**/*.json'):
            record = json.load(open(json_file))
            date = datetime(year=int(record['header']['year']),
                            month=month_map[record['header']['month']],
                            day=int(record['header']['day']))
            doc_id = record['id']
            doc_title = record['doc_title']
            for entry in record['content']:
                if entry['kind'] != 'speech':
                    continue
                schema['doc_title'].append(doc_title)
                schema['doc_id'].append(doc_id)
                schema['date'].append(date)
                schema['turn'].append(entry['turn'])
                schema['speaker'].append(entry['speaker'])
                schema['text'].append(entry['text'])
                schema['speaker_bioguide'].append(entry['speaker_bioguide'])

        df = pd.DataFrame.from_dict(schema)
        df.to_csv('./data.csv')


if __name__ == "__main__":
    main()
