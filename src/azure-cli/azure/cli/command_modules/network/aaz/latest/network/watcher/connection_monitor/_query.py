# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network watcher connection-monitor query",
)
class Query(AAZCommand):
    """Query a snapshot of the most recent connection state of a connection monitor.

    :example: List a connection monitor for the given region.
        az network watcher connection-monitor query -l westus -n MyConnectionMonitorName
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkwatchers/{}/connectionmonitors/{}/query", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.connection_monitor_name = AAZStrArg(
            options=["-n", "--name", "--connection-monitor-name"],
            help="Connection monitor name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.network_watcher_name = AAZStrArg(
            options=["--network-watcher-name"],
            help="The name of the Network Watcher resource.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group_name = AAZResourceGroupNameArg(
            options=["-g", "--resource-group-name"],
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ConnectionMonitorsQuery(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ConnectionMonitorsQuery(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/query",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "connectionMonitorName", self.ctx.args.connection_monitor_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkWatcherName", self.ctx.args.network_watcher_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _QueryHelper._build_schema_connection_monitor_query_result_read(cls._schema_on_200)

            return cls._schema_on_200


class _QueryHelper:
    """Helper class for Query"""

    _schema_connection_monitor_query_result_read = None

    @classmethod
    def _build_schema_connection_monitor_query_result_read(cls, _schema):
        if cls._schema_connection_monitor_query_result_read is not None:
            _schema.source_status = cls._schema_connection_monitor_query_result_read.source_status
            _schema.states = cls._schema_connection_monitor_query_result_read.states
            return

        cls._schema_connection_monitor_query_result_read = _schema_connection_monitor_query_result_read = AAZObjectType()

        connection_monitor_query_result_read = _schema_connection_monitor_query_result_read
        connection_monitor_query_result_read.source_status = AAZStrType(
            serialized_name="sourceStatus",
        )
        connection_monitor_query_result_read.states = AAZListType()

        states = _schema_connection_monitor_query_result_read.states
        states.Element = AAZObjectType()

        _element = _schema_connection_monitor_query_result_read.states.Element
        _element.avg_latency_in_ms = AAZIntType(
            serialized_name="avgLatencyInMs",
        )
        _element.connection_state = AAZStrType(
            serialized_name="connectionState",
        )
        _element.end_time = AAZStrType(
            serialized_name="endTime",
        )
        _element.evaluation_state = AAZStrType(
            serialized_name="evaluationState",
        )
        _element.hops = AAZListType(
            flags={"read_only": True},
        )
        _element.max_latency_in_ms = AAZIntType(
            serialized_name="maxLatencyInMs",
        )
        _element.min_latency_in_ms = AAZIntType(
            serialized_name="minLatencyInMs",
        )
        _element.probes_failed = AAZIntType(
            serialized_name="probesFailed",
        )
        _element.probes_sent = AAZIntType(
            serialized_name="probesSent",
        )
        _element.start_time = AAZStrType(
            serialized_name="startTime",
        )

        hops = _schema_connection_monitor_query_result_read.states.Element.hops
        hops.Element = AAZObjectType()

        _element = _schema_connection_monitor_query_result_read.states.Element.hops.Element
        _element.address = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType(
            flags={"read_only": True},
        )
        _element.issues = AAZListType(
            flags={"read_only": True},
        )
        _element.links = AAZListType(
            flags={"read_only": True},
        )
        _element.next_hop_ids = AAZListType(
            serialized_name="nextHopIds",
            flags={"read_only": True},
        )
        _element.previous_hop_ids = AAZListType(
            serialized_name="previousHopIds",
            flags={"read_only": True},
        )
        _element.previous_links = AAZListType(
            serialized_name="previousLinks",
            flags={"read_only": True},
        )
        _element.resource_id = AAZStrType(
            serialized_name="resourceId",
            flags={"read_only": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        issues = _schema_connection_monitor_query_result_read.states.Element.hops.Element.issues
        issues.Element = AAZObjectType()
        cls._build_schema_connectivity_issue_read(issues.Element)

        links = _schema_connection_monitor_query_result_read.states.Element.hops.Element.links
        links.Element = AAZObjectType()
        cls._build_schema_hop_link_read(links.Element)

        next_hop_ids = _schema_connection_monitor_query_result_read.states.Element.hops.Element.next_hop_ids
        next_hop_ids.Element = AAZStrType()

        previous_hop_ids = _schema_connection_monitor_query_result_read.states.Element.hops.Element.previous_hop_ids
        previous_hop_ids.Element = AAZStrType()

        previous_links = _schema_connection_monitor_query_result_read.states.Element.hops.Element.previous_links
        previous_links.Element = AAZObjectType()
        cls._build_schema_hop_link_read(previous_links.Element)

        _schema.source_status = cls._schema_connection_monitor_query_result_read.source_status
        _schema.states = cls._schema_connection_monitor_query_result_read.states

    _schema_connectivity_issue_read = None

    @classmethod
    def _build_schema_connectivity_issue_read(cls, _schema):
        if cls._schema_connectivity_issue_read is not None:
            _schema.context = cls._schema_connectivity_issue_read.context
            _schema.origin = cls._schema_connectivity_issue_read.origin
            _schema.severity = cls._schema_connectivity_issue_read.severity
            _schema.type = cls._schema_connectivity_issue_read.type
            return

        cls._schema_connectivity_issue_read = _schema_connectivity_issue_read = AAZObjectType()

        connectivity_issue_read = _schema_connectivity_issue_read
        connectivity_issue_read.context = AAZListType(
            flags={"read_only": True},
        )
        connectivity_issue_read.origin = AAZStrType(
            flags={"read_only": True},
        )
        connectivity_issue_read.severity = AAZStrType(
            flags={"read_only": True},
        )
        connectivity_issue_read.type = AAZStrType(
            flags={"read_only": True},
        )

        context = _schema_connectivity_issue_read.context
        context.Element = AAZDictType()

        _element = _schema_connectivity_issue_read.context.Element
        _element.Element = AAZStrType()

        _schema.context = cls._schema_connectivity_issue_read.context
        _schema.origin = cls._schema_connectivity_issue_read.origin
        _schema.severity = cls._schema_connectivity_issue_read.severity
        _schema.type = cls._schema_connectivity_issue_read.type

    _schema_hop_link_read = None

    @classmethod
    def _build_schema_hop_link_read(cls, _schema):
        if cls._schema_hop_link_read is not None:
            _schema.context = cls._schema_hop_link_read.context
            _schema.issues = cls._schema_hop_link_read.issues
            _schema.link_type = cls._schema_hop_link_read.link_type
            _schema.next_hop_id = cls._schema_hop_link_read.next_hop_id
            _schema.properties = cls._schema_hop_link_read.properties
            _schema.resource_id = cls._schema_hop_link_read.resource_id
            return

        cls._schema_hop_link_read = _schema_hop_link_read = AAZObjectType()

        hop_link_read = _schema_hop_link_read
        hop_link_read.context = AAZDictType(
            flags={"read_only": True},
        )
        hop_link_read.issues = AAZListType(
            flags={"read_only": True},
        )
        hop_link_read.link_type = AAZStrType(
            serialized_name="linkType",
            flags={"read_only": True},
        )
        hop_link_read.next_hop_id = AAZStrType(
            serialized_name="nextHopId",
            flags={"read_only": True},
        )
        hop_link_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        hop_link_read.resource_id = AAZStrType(
            serialized_name="resourceId",
            flags={"read_only": True},
        )

        context = _schema_hop_link_read.context
        context.Element = AAZStrType()

        issues = _schema_hop_link_read.issues
        issues.Element = AAZObjectType()
        cls._build_schema_connectivity_issue_read(issues.Element)

        properties = _schema_hop_link_read.properties
        properties.round_trip_time_avg = AAZIntType(
            serialized_name="roundTripTimeAvg",
            flags={"read_only": True},
        )
        properties.round_trip_time_max = AAZIntType(
            serialized_name="roundTripTimeMax",
            flags={"read_only": True},
        )
        properties.round_trip_time_min = AAZIntType(
            serialized_name="roundTripTimeMin",
            flags={"read_only": True},
        )

        _schema.context = cls._schema_hop_link_read.context
        _schema.issues = cls._schema_hop_link_read.issues
        _schema.link_type = cls._schema_hop_link_read.link_type
        _schema.next_hop_id = cls._schema_hop_link_read.next_hop_id
        _schema.properties = cls._schema_hop_link_read.properties
        _schema.resource_id = cls._schema_hop_link_read.resource_id


__all__ = ["Query"]