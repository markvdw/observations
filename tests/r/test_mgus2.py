from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mgus2 import mgus2


def test_mgus2():
  """Test module mgus2.py by downloading
   mgus2.csv and testing shape of
   extracted data has 1384 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mgus2(test_path)
  try:
    assert x_train.shape == (1384, 10)
  except:
    shutil.rmtree(test_path)
    raise()
