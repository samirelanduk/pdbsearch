import json
import argparse
from pdbsearch.schema import fetch_names_from_rcsb_schema

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="mode", required=True)
    schema_parser = subparsers.add_parser("schema", help="Fetch and process schema")
    schema_parser.add_argument("--chemical", action="store_true", help="Use chemical schema")
    schema_parser.add_argument("--indent", type=int, default=None, help="JSON indentation")
    args = parser.parse_args()
    if args.mode == "schema":
        names = fetch_names_from_rcsb_schema(chemical=args.chemical)
        print(json.dumps(names, indent=args.indent))


if __name__ == "__main__":
    main()