from omegaconf import DictConfig, ListConfig, OmegaConf
import argparse
from models import build_model
from datasets import build_loader
from trainers import build_trainer
import logging


def select_log_level(level):
    """ Selects the log level based on the input string
    """
    if level == "debug":
        level = logging.DEBUG
    elif level == "info":
        level = logging.INFO
    elif level == "warning":
        level = logging.WARNING
    elif level == "error":
        level = logging.ERROR
    elif level == "critical":
        level = logging.CRITICAL

    logging.basicConfig(level=level)


def get_config():
	"""	Creates a config object from the yaml file and the cli arguments
	"""
	cli_conf = OmegaConf.from_cli()

	yaml_conf = OmegaConf.load(cli_conf.config)
	conf = OmegaConf.merge(yaml_conf, cli_conf)
	return conf



if __name__=="__main__":
    
    cfg = get_config()
    
    # log level
    select_log_level(cfg.experiment.log_level)
    
    # build the model, data loader and trainer
    model = build_model(cfg)
    data_loaders = build_loader(cfg)
    trainer = build_trainer(cfg, model, data_loaders)
    
    # train the model
    trainer.train()
    
    
  
    