#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jerry Bai'

import unittest
from unittest import mock

import mock_import
import foo


class TestImport(unittest.TestCase):

    def setUp(self):
        print("Test class set up")

    def test_load_image(self):
        # mock_imread = mock.patch('cv2.imread')
        with mock.patch.object(foo.cv2, 'imread') as mock_imread:
            foo.load_image('test')
            mock_imread.assert_called_with('test')