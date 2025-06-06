#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# coding: utf-8

# flake8: noqa

"""
    Polaris Management Service

    Defines the management APIs for using Polaris to create and manage Iceberg catalogs and their principals

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from polaris.management.api.polaris_default_api import PolarisDefaultApi

# import ApiClient
from polaris.management.api_response import ApiResponse
from polaris.management.api_client import ApiClient
from polaris.management.configuration import Configuration
from polaris.management.exceptions import OpenApiException
from polaris.management.exceptions import ApiTypeError
from polaris.management.exceptions import ApiValueError
from polaris.management.exceptions import ApiKeyError
from polaris.management.exceptions import ApiAttributeError
from polaris.management.exceptions import ApiException

# import models into sdk package
from polaris.management.models.add_grant_request import AddGrantRequest
from polaris.management.models.authentication_parameters import AuthenticationParameters
from polaris.management.models.aws_iam_service_identity_info import AwsIamServiceIdentityInfo
from polaris.management.models.aws_storage_config_info import AwsStorageConfigInfo
from polaris.management.models.azure_storage_config_info import AzureStorageConfigInfo
from polaris.management.models.bearer_authentication_parameters import BearerAuthenticationParameters
from polaris.management.models.catalog import Catalog
from polaris.management.models.catalog_grant import CatalogGrant
from polaris.management.models.catalog_privilege import CatalogPrivilege
from polaris.management.models.catalog_properties import CatalogProperties
from polaris.management.models.catalog_role import CatalogRole
from polaris.management.models.catalog_roles import CatalogRoles
from polaris.management.models.catalogs import Catalogs
from polaris.management.models.connection_config_info import ConnectionConfigInfo
from polaris.management.models.create_catalog_request import CreateCatalogRequest
from polaris.management.models.create_catalog_role_request import CreateCatalogRoleRequest
from polaris.management.models.create_principal_request import CreatePrincipalRequest
from polaris.management.models.create_principal_role_request import CreatePrincipalRoleRequest
from polaris.management.models.external_catalog import ExternalCatalog
from polaris.management.models.file_storage_config_info import FileStorageConfigInfo
from polaris.management.models.gcp_storage_config_info import GcpStorageConfigInfo
from polaris.management.models.grant_catalog_role_request import GrantCatalogRoleRequest
from polaris.management.models.grant_principal_role_request import GrantPrincipalRoleRequest
from polaris.management.models.grant_resource import GrantResource
from polaris.management.models.grant_resources import GrantResources
from polaris.management.models.hadoop_connection_config_info import HadoopConnectionConfigInfo
from polaris.management.models.iceberg_rest_connection_config_info import IcebergRestConnectionConfigInfo
from polaris.management.models.namespace_grant import NamespaceGrant
from polaris.management.models.namespace_privilege import NamespacePrivilege
from polaris.management.models.o_auth_client_credentials_parameters import OAuthClientCredentialsParameters
from polaris.management.models.polaris_catalog import PolarisCatalog
from polaris.management.models.policy_grant import PolicyGrant
from polaris.management.models.policy_privilege import PolicyPrivilege
from polaris.management.models.principal import Principal
from polaris.management.models.principal_role import PrincipalRole
from polaris.management.models.principal_roles import PrincipalRoles
from polaris.management.models.principal_with_credentials import PrincipalWithCredentials
from polaris.management.models.principal_with_credentials_credentials import PrincipalWithCredentialsCredentials
from polaris.management.models.principals import Principals
from polaris.management.models.revoke_grant_request import RevokeGrantRequest
from polaris.management.models.service_identity_info import ServiceIdentityInfo
from polaris.management.models.sig_v4_authentication_parameters import SigV4AuthenticationParameters
from polaris.management.models.storage_config_info import StorageConfigInfo
from polaris.management.models.table_grant import TableGrant
from polaris.management.models.table_privilege import TablePrivilege
from polaris.management.models.update_catalog_request import UpdateCatalogRequest
from polaris.management.models.update_catalog_role_request import UpdateCatalogRoleRequest
from polaris.management.models.update_principal_request import UpdatePrincipalRequest
from polaris.management.models.update_principal_role_request import UpdatePrincipalRoleRequest
from polaris.management.models.view_grant import ViewGrant
from polaris.management.models.view_privilege import ViewPrivilege
