import os
import sys

# Add path.
# See:
# https://www.magata.net/memo/index.php?pytest%C6%FE%CC%E7#y2046859
bot_path = os.path.dirname(os.path.abspath(__file__)) + '/../bot/'
sys.path.append(os.path.abspath(bot_path))
