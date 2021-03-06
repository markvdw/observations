from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.quartet import quartet


def test_quartet():
  """Test module quartet.py by downloading
   quartet.csv and testing shape of
   extracted data has 11 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = quartet(test_path)
  try:
    assert x_train.shape == (11, 6)
  except:
    shutil.rmtree(test_path)
    raise()
