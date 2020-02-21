from knack.util import CLIError
from msal import ClientApplication


class SSHCertificateClientApplication(ClientApplication):

    def _acquire_token_silent_by_finding_rt_belongs_to_me_or_my_family(
            self, authority, scopes, account, **kwargs):
        return self._acquire_token_silent_by_finding_specific_refresh_token(
            authority, scopes, **kwargs)

    def _acquire_token_silent_by_finding_specific_refresh_token(
            self, authority, scopes, **kwargs):
        refresh_token = kwargs.get('refresh_token', None)
        client = self._build_client(self.client_credential, authority)
        kwargs.pop('refresh_token')
        response = client.obtain_token_by_refresh_token(refresh_token, scope=scopes, **kwargs)
        if "error" in response:
            raise CLIError(response["error"])
        return response
