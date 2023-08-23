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
    "vmss rolling-upgrade get-latest",
)
class GetLatest(AAZCommand):
    """Get the status of the latest virtual machine scale set rolling upgrade.
    """

    _aaz_info = {
        "version": "2022-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/virtualmachinescalesets/{}/rollingupgrades/latest", "2022-11-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.",
            required=True,
        )
        _args_schema.virtual_machine_scale_set_name = AAZStrArg(
            options=["-n", "--name", "--vm-scale-set-name", "--virtual-machine-scale-set-name"],
            help="Scale set name. You can configure the default using `az configure --defaults vmss=<name>`.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualMachineScaleSetRollingUpgradesGetLatest(ctx=self.ctx)()
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

    class VirtualMachineScaleSetRollingUpgradesGetLatest(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/latest",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "vmScaleSetName", self.ctx.args.virtual_machine_scale_set_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.error = AAZObjectType()
            _GetLatestHelper._build_schema_api_error_read(properties.error)
            properties.policy = AAZObjectType()
            properties.progress = AAZObjectType()
            properties.running_status = AAZObjectType(
                serialized_name="runningStatus",
            )

            policy = cls._schema_on_200.properties.policy
            policy.enable_cross_zone_upgrade = AAZBoolType(
                serialized_name="enableCrossZoneUpgrade",
            )
            policy.max_batch_instance_percent = AAZIntType(
                serialized_name="maxBatchInstancePercent",
            )
            policy.max_surge = AAZBoolType(
                serialized_name="maxSurge",
            )
            policy.max_unhealthy_instance_percent = AAZIntType(
                serialized_name="maxUnhealthyInstancePercent",
            )
            policy.max_unhealthy_upgraded_instance_percent = AAZIntType(
                serialized_name="maxUnhealthyUpgradedInstancePercent",
            )
            policy.pause_time_between_batches = AAZStrType(
                serialized_name="pauseTimeBetweenBatches",
            )
            policy.prioritize_unhealthy_instances = AAZBoolType(
                serialized_name="prioritizeUnhealthyInstances",
            )
            policy.rollback_failed_instances_on_policy_breach = AAZBoolType(
                serialized_name="rollbackFailedInstancesOnPolicyBreach",
            )

            progress = cls._schema_on_200.properties.progress
            progress.failed_instance_count = AAZIntType(
                serialized_name="failedInstanceCount",
                flags={"read_only": True},
            )
            progress.in_progress_instance_count = AAZIntType(
                serialized_name="inProgressInstanceCount",
                flags={"read_only": True},
            )
            progress.pending_instance_count = AAZIntType(
                serialized_name="pendingInstanceCount",
                flags={"read_only": True},
            )
            progress.successful_instance_count = AAZIntType(
                serialized_name="successfulInstanceCount",
                flags={"read_only": True},
            )

            running_status = cls._schema_on_200.properties.running_status
            running_status.code = AAZStrType(
                flags={"read_only": True},
            )
            running_status.last_action = AAZStrType(
                serialized_name="lastAction",
                flags={"read_only": True},
            )
            running_status.last_action_time = AAZStrType(
                serialized_name="lastActionTime",
                flags={"read_only": True},
            )
            running_status.start_time = AAZStrType(
                serialized_name="startTime",
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _GetLatestHelper:
    """Helper class for GetLatest"""

    _schema_api_error_read = None

    @classmethod
    def _build_schema_api_error_read(cls, _schema):
        if cls._schema_api_error_read is not None:
            _schema.code = cls._schema_api_error_read.code
            _schema.details = cls._schema_api_error_read.details
            _schema.innererror = cls._schema_api_error_read.innererror
            _schema.message = cls._schema_api_error_read.message
            _schema.target = cls._schema_api_error_read.target
            return

        cls._schema_api_error_read = _schema_api_error_read = AAZObjectType()

        api_error_read = _schema_api_error_read
        api_error_read.code = AAZStrType()
        api_error_read.details = AAZListType()
        api_error_read.innererror = AAZObjectType()
        api_error_read.message = AAZStrType()
        api_error_read.target = AAZStrType()

        details = _schema_api_error_read.details
        details.Element = AAZObjectType()

        _element = _schema_api_error_read.details.Element
        _element.code = AAZStrType()
        _element.message = AAZStrType()
        _element.target = AAZStrType()

        innererror = _schema_api_error_read.innererror
        innererror.errordetail = AAZStrType()
        innererror.exceptiontype = AAZStrType()

        _schema.code = cls._schema_api_error_read.code
        _schema.details = cls._schema_api_error_read.details
        _schema.innererror = cls._schema_api_error_read.innererror
        _schema.message = cls._schema_api_error_read.message
        _schema.target = cls._schema_api_error_read.target


__all__ = ["GetLatest"]