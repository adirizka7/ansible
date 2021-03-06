# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


class ModuleDocFragment(object):
    # Postgres documentation fragment
    DOCUMENTATION = r'''
options:
  login_user:
    description:
      - The username used to authenticate with.
    type: str
    default: postgres
  login_password:
    description:
      - The password used to authenticate with.
    type: str
  login_host:
    description:
      - Host running the database.
    type: str
  login_unix_socket:
    description:
      - Path to a Unix domain socket for local connections.
    type: path
  port:
    description:
      - Database port to connect to.
    type: int
    default: 5432
  ssl_mode:
    description:
      - Determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the server.
      - See https://www.postgresql.org/docs/current/static/libpq-ssl.html for more information on the modes.
      - Default of C(prefer) matches libpq default.
    type: str
    default: prefer
    choices: [ allow, disable, prefer, require, verify-ca, verify-full ]
    version_added: '2.3'
  ssl_rootcert:
    description:
      - Specifies the name of a file containing SSL certificate authority (CA) certificate(s).
      - If the file exists, the server's certificate will be verified to be signed by one of these authorities.
    type: path
    version_added: '2.3'
notes:
- The default authentication assumes that you are either logging in as or sudo'ing to the C(postgres) account on the host.
- This module uses I(psycopg2), a Python PostgreSQL database adapter. You must ensure that psycopg2 is installed on
  the host before using this module. If the remote host is the PostgreSQL server (which is the default case), then
  PostgreSQL must also be installed on the remote host. For Ubuntu-based systems, install the C(postgresql), C(libpq-dev),
  and C(python-psycopg2) packages on the remote host before using this module.
- The ssl_rootcert parameter requires at least Postgres version 8.4 and I(psycopg2) version 2.4.3.
requirements: [ psycopg2 ]
'''
