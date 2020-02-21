# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack import log


logger = log.get_logger(__name__)


def get_ssh_credentials(cli_ctx, modulus, exponent):
    from azure.cli.core._profile import Profile
    logger.debug("Getting SSH credentials")
    profile = Profile(cli_ctx=cli_ctx)

    user, cert = profile.get_ssh_credentials(modulus, exponent)
    return SSHCredentials(user, cert)


class SSHCredentials(object):
    def __init__(self, username, cert):
        self.username = username
        self.certificate = "ssh-rsa-cert-v01@openssh.com " + cert