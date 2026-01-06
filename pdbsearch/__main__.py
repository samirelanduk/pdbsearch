import json
import argparse
from pdbsearch.schema import fetch_names_from_rcsb_schema, clear_cached_terms

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="mode", required=True)
    schema_parser = subparsers.add_parser("schema", help="Fetch and process schema")
    schema_parser.add_argument("--chemical", action="store_true", help="Use chemical schema")
    schema_parser.add_argument("--indent", type=int, default=None, help="JSON indentation")
    subparsers.add_parser("clearschema", help="Clear cached terms")
    args = parser.parse_args()
    if args.mode == "schema":
        names = fetch_names_from_rcsb_schema(chemical=args.chemical)
        print(json.dumps(names, indent=args.indent))
    elif args.mode == "clearschema":
        clear_cached_terms()


if __name__ == "__main__":
    main()