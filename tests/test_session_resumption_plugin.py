import unittest
from sslyze.plugins.session_renegotiation_plugin import SessionRenegotiationPlugin
from sslyze.plugins.session_resumption_plugin import SessionResumptionPlugin
from sslyze.server_connectivity import ServerConnectivityInfo


class SessionResumptionPluginPluginTestCase(unittest.TestCase):

    def test_resumption(self):
        server_info = ServerConnectivityInfo(hostname='www.google.com')
        server_info.test_connectivity_to_server()

        plugin = SessionResumptionPlugin()
        plugin_result = plugin.process_task(server_info, 'resum')

        self.assertTrue(plugin_result.is_ticket_resumption_supported)
        self.assertTrue(plugin_result.attempted_resumptions_nb)
        self.assertTrue(plugin_result.successful_resumptions_nb)
        self.assertFalse(plugin_result.errored_resumptions_list)

        self.assertTrue(plugin_result.as_text())
        self.assertTrue(plugin_result.as_xml())

