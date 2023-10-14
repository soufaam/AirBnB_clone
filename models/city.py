#!/usr/bin/python3
"""
city module that includes City class
"""

import models
from models.base_model import BaseModel



class City(BaseModel):
    """city class"""

    state_id = ''
    name = ''
