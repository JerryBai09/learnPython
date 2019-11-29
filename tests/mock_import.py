#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jerry Bai'

import sys
from unittest import mock

sys.modules['cv2'] = mock.MagicMock()