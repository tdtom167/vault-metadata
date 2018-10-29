import argparse
import os
import pprint
import voluptuous
import yaml
from utils import schema_metadata
pp = pprint.PrettyPrinter(indent=6)

def parse_args():
    parser = argparse.ArgumentParser(description='Query YAML tool')
    parser.add_argument('-s', '--subtree', action="store", default=os.getcwd(), help="Subtree in which to search")
    parser.add_argument('-p', '--pattern', action="store", default='', help="Pattern according to which search names")
    parser.add_argument('-d', '--data', action="store", help="Data for which search the files")
    parser.add_argument('-m', '--meta', action="store_true", help="If we want to show metadata")
    return parser.parse_args()

def list_rec(args,files):
    for root, filename in files:
        docs = yaml.load_all(open(os.path.join(root,filename), "r"))
        for conf in list(docs):
            name = next(iter(conf))
            if args.pattern in name:
                if args.data:
                    for key, val in conf[name].iteritems():
                        if args.data in key or args.data in val:
                            print name, key, val
                else:
                    print name
                    if args.meta:
                        pp.pprint(conf[name])

def check_config(args, files):
    schema = voluptuous.Schema(schema_metadata)
    for root, filename in files:
        try:
            docs = yaml.load_all(open(os.path.join(root,filename), "r"))
            for conf in list(docs):
                schema(conf)
        except Exception as e:
            print root, filename, e

def get_meta_files(args):
    meta_files = []
    for root, _, files in os.walk(args.subtree):
        for filename in files:
            if 'META' in filename:
                tupl = (root,filename)
                meta_files.append(tupl)
    return meta_files

args = parse_args()
files = get_meta_files(args)
check_config(args, files)
list_rec(args, files)
