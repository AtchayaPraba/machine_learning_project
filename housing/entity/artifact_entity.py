from collections import namedtuple

from housing.entity.config_entity import DataIngestionConfig

DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path","test_file_path","is_ingested","message"])
