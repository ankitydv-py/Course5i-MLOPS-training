import os
import yaml
import pandas as pd
import argparse
from pkgutil import get_data # helpful in passing parameters

def get_data(config_path):
    config=read_params(config_path)
    # print(config)
    data_path=config["data_source"]["s3_source"]
    df=pd.read_csv(data_path, sep=",",encoding='utf-8')
    # print(df.head())
    return df

def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
        return config


if __name__ == "__main__": # execute code when file runs as script
    args = argparse.ArgumentParser()
    args.add_argument("--config", default= "params.yaml") # calling default file
    parsed_args = args.parse_args()
    data=get_data(config_path=parsed_args.config)
 