# coding: utf-8

from pub import app

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)
