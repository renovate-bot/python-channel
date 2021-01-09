# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.cloud.channel_v1.types import (
    channel_partner_links as gcc_channel_partner_links,
)
from google.cloud.channel_v1.types import common
from google.cloud.channel_v1.types import customers as gcc_customers
from google.cloud.channel_v1.types import entitlements as gcc_entitlements
from google.cloud.channel_v1.types import offers as gcc_offers
from google.cloud.channel_v1.types import products as gcc_products
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.channel.v1",
    manifest={
        "CheckCloudIdentityAccountsExistRequest",
        "CloudIdentityCustomerAccount",
        "CheckCloudIdentityAccountsExistResponse",
        "ListCustomersRequest",
        "ListCustomersResponse",
        "GetCustomerRequest",
        "CreateCustomerRequest",
        "UpdateCustomerRequest",
        "DeleteCustomerRequest",
        "ProvisionCloudIdentityRequest",
        "ListEntitlementsRequest",
        "ListEntitlementsResponse",
        "ListTransferableSkusRequest",
        "ListTransferableSkusResponse",
        "ListTransferableOffersRequest",
        "ListTransferableOffersResponse",
        "TransferableOffer",
        "GetEntitlementRequest",
        "ListChannelPartnerLinksRequest",
        "ListChannelPartnerLinksResponse",
        "GetChannelPartnerLinkRequest",
        "CreateChannelPartnerLinkRequest",
        "UpdateChannelPartnerLinkRequest",
        "CreateEntitlementRequest",
        "TransferEntitlementsRequest",
        "TransferEntitlementsResponse",
        "TransferEntitlementsToGoogleRequest",
        "ChangeParametersRequest",
        "ChangeRenewalSettingsRequest",
        "ChangeOfferRequest",
        "StartPaidServiceRequest",
        "CancelEntitlementRequest",
        "SuspendEntitlementRequest",
        "ActivateEntitlementRequest",
        "ListProductsRequest",
        "ListProductsResponse",
        "ListSkusRequest",
        "ListSkusResponse",
        "ListOffersRequest",
        "ListOffersResponse",
        "ListPurchasableSkusRequest",
        "ListPurchasableSkusResponse",
        "PurchasableSku",
        "ListPurchasableOffersRequest",
        "ListPurchasableOffersResponse",
        "PurchasableOffer",
    },
)


class CheckCloudIdentityAccountsExistRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CheckCloudIdentityAccountsExist][google.cloud.channel.v1.CloudChannelService.CheckCloudIdentityAccountsExist].

    Attributes:
        parent (str):
            Required. The resource name of the reseller account. The
            parent takes the format: accounts/{account_id}
        domain (str):
            Required. Domain for which the Cloud Identity
            account customer is fetched.
    """

    parent = proto.Field(proto.STRING, number=1)

    domain = proto.Field(proto.STRING, number=2)


class CloudIdentityCustomerAccount(proto.Message):
    r"""Entity representing a Cloud Identity account which may or may
    not be associated with a Channel Services API partner.

    Attributes:
        existing (bool):
            True if a Cloud Identity account exists for a
            specific domain.
        owned (bool):
            True if the Cloud Identity account is
            associated with a customer belonging to the
            Channel Services partner making the API call.
        customer_name (str):
            Name of the customer that owns the Cloud Identity account.
            This field is populated ONLY if owned = true. The
            customer_name takes the format:
            accounts/{account_id}/customers/{customer_id}
        customer_cloud_identity_id (str):
            Cloud Identity ID of the customer. This field
            is populated ONLY if existing = true.
    """

    existing = proto.Field(proto.BOOL, number=1)

    owned = proto.Field(proto.BOOL, number=2)

    customer_name = proto.Field(proto.STRING, number=3)

    customer_cloud_identity_id = proto.Field(proto.STRING, number=4)


class CheckCloudIdentityAccountsExistResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.CheckCloudIdentityAccountsExist][google.cloud.channel.v1.CloudChannelService.CheckCloudIdentityAccountsExist].

    Attributes:
        cloud_identity_accounts (Sequence[google.cloud.channel_v1.types.CloudIdentityCustomerAccount]):
            The Cloud Identity accounts associated with
            the domain.
    """

    cloud_identity_accounts = proto.RepeatedField(
        proto.MESSAGE, number=1, message="CloudIdentityCustomerAccount",
    )


class ListCustomersRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListCustomers][google.cloud.channel.v1.CloudChannelService.ListCustomers]

    Attributes:
        parent (str):
            Required. The resource name of the reseller account from
            which to list customers. The parent takes the format:
            accounts/{account_id}.
        page_size (int):
            Optional. The maximum number of customers to
            return. The service may return fewer than this
            value. If unspecified, at most 10 customers will
            be returned. The maximum value is 50; values
            about 50 will be coerced to 50.
        page_token (str):
            Optional. A token identifying a page of results, if other
            than the first one. Typically obtained via
            [ListCustomersResponse.next_page_token][google.cloud.channel.v1.ListCustomersResponse.next_page_token]
            of the previous
            [CloudChannelService.ListCustomers][google.cloud.channel.v1.CloudChannelService.ListCustomers]
            call.
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)


class ListCustomersResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListCustomers][google.cloud.channel.v1.CloudChannelService.ListCustomers].

    Attributes:
        customers (Sequence[google.cloud.channel_v1.types.Customer]):
            The customers belonging to the reseller or
            distributor.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListCustomersRequest.page_token][google.cloud.channel.v1.ListCustomersRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    customers = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gcc_customers.Customer,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class GetCustomerRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.GetCustomer][google.cloud.channel.v1.CloudChannelService.GetCustomer].

    Attributes:
        name (str):
            Required. The resource name of the customer to retrieve. The
            name takes the format:
            accounts/{account_id}/customers/{customer_id}
    """

    name = proto.Field(proto.STRING, number=1)


class CreateCustomerRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CreateCustomer][google.cloud.channel.v1.CloudChannelService.CreateCustomer]

    Attributes:
        parent (str):
            Required. The resource name of reseller account in which to
            create the customer. The parent takes the format:
            accounts/{account_id}
        customer (google.cloud.channel_v1.types.Customer):
            Required. The customer to create.
    """

    parent = proto.Field(proto.STRING, number=1)

    customer = proto.Field(proto.MESSAGE, number=2, message=gcc_customers.Customer,)


class UpdateCustomerRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.UpdateCustomer][google.cloud.channel.v1.CloudChannelService.UpdateCustomer].

    Attributes:
        customer (google.cloud.channel_v1.types.Customer):
            Required. New contents of the customer.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask that applies to the resource.
            Optional.
    """

    customer = proto.Field(proto.MESSAGE, number=2, message=gcc_customers.Customer,)

    update_mask = proto.Field(proto.MESSAGE, number=3, message=field_mask.FieldMask,)


class DeleteCustomerRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.DeleteCustomer][google.cloud.channel.v1.CloudChannelService.DeleteCustomer].

    Attributes:
        name (str):
            Required. The resource name of the customer
            to delete.
    """

    name = proto.Field(proto.STRING, number=1)


class ProvisionCloudIdentityRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ProvisionCloudIdentity][google.cloud.channel.v1.CloudChannelService.ProvisionCloudIdentity]

    Attributes:
        customer (str):
            Required. Resource name of the customer. Format:
            accounts/{account_id}/customers/{customer_id}
        cloud_identity_info (google.cloud.channel_v1.types.CloudIdentityInfo):
            CloudIdentity-specific customer information.
        user (google.cloud.channel_v1.types.AdminUser):
            Admin user information.
        validate_only (bool):
            If set, validate the request and preview the
            review, but do not actually post it.
    """

    customer = proto.Field(proto.STRING, number=1)

    cloud_identity_info = proto.Field(
        proto.MESSAGE, number=2, message=common.CloudIdentityInfo,
    )

    user = proto.Field(proto.MESSAGE, number=3, message=common.AdminUser,)

    validate_only = proto.Field(proto.BOOL, number=4)


class ListEntitlementsRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListEntitlements][google.cloud.channel.v1.CloudChannelService.ListEntitlements]

    Attributes:
        parent (str):
            Required. The resource name of the reseller's customer
            account for which to list entitlements. The parent takes the
            format: accounts/{account_id}/customers/{customer_id}
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, at most 50 entitlements will be
            returned. The maximum value is 100; values above
            100 will be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of results, if other
            than the first one. Typically obtained via
            [ListEntitlementsResponse.next_page_token][google.cloud.channel.v1.ListEntitlementsResponse.next_page_token]
            of the previous
            [CloudChannelService.ListEntitlements][google.cloud.channel.v1.CloudChannelService.ListEntitlements]
            call.
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)


class ListEntitlementsResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListEntitlements][google.cloud.channel.v1.CloudChannelService.ListEntitlements].

    Attributes:
        entitlements (Sequence[google.cloud.channel_v1.types.Entitlement]):
            The entitlements belonging to the reseller's
            customer.
        next_page_token (str):
            A token to List next page of results. Pass to
            [ListEntitlementsRequest.page_token][google.cloud.channel.v1.ListEntitlementsRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    entitlements = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gcc_entitlements.Entitlement,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class ListTransferableSkusRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListTransferableSkus][google.cloud.channel.v1.CloudChannelService.ListTransferableSkus]

    Attributes:
        cloud_identity_id (str):
            Customer's Cloud Identity ID
        customer_name (str):
            A reseller is required to create a customer and use the
            resource name of the created customer here. The
            customer_name takes the format:
            accounts/{account_id}/customers/{customer_id}
        parent (str):
            Required. The resource name of the reseller's account. The
            parent takes the format: accounts/{account_id}
        page_size (int):
            Requested page size. Server might return
            fewer results than requested. If unspecified, at
            most 100 SKUs will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000. Optional.
        page_token (str):
            A token identifying a page of results, if other than the
            first one. Typically obtained via
            [ListTransferableSkusResponse.next_page_token][google.cloud.channel.v1.ListTransferableSkusResponse.next_page_token]
            of the previous
            [CloudChannelService.ListTransferableSkus][google.cloud.channel.v1.CloudChannelService.ListTransferableSkus]
            call. Optional.
        auth_token (str):
            This token is generated by the Super Admin of
            the resold customer to authorize a reseller to
            access their Cloud Identity and purchase
            entitlements on their behalf. This token can be
            omitted once the authorization is generated. See
            https://support.google.com/a/answer/7643790 for
            more details.
        language_code (str):
            The BCP-47 language code, such as "en-US".
            If specified, the response will be localized to
            the corresponding language code. Default is "en-
            US".
            Optional.
    """

    cloud_identity_id = proto.Field(
        proto.STRING, number=4, oneof="transferred_customer_identity"
    )

    customer_name = proto.Field(
        proto.STRING, number=7, oneof="transferred_customer_identity"
    )

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)

    auth_token = proto.Field(proto.STRING, number=5)

    language_code = proto.Field(proto.STRING, number=6)


class ListTransferableSkusResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListTransferableSkus][google.cloud.channel.v1.CloudChannelService.ListTransferableSkus].

    Attributes:
        transferable_skus (Sequence[google.cloud.channel_v1.types.TransferableSku]):
            Information about existing SKUs for a
            customer that would need to be transferred.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListTransferableSkusRequest.page_token][google.cloud.channel.v1.ListTransferableSkusRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    transferable_skus = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gcc_entitlements.TransferableSku,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class ListTransferableOffersRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListTransferableOffers][google.cloud.channel.v1.CloudChannelService.ListTransferableOffers]

    Attributes:
        cloud_identity_id (str):
            Customer's Cloud Identity ID
        customer_name (str):
            A reseller should create a customer and use
            the resource name of the created customer here.
        parent (str):
            Required. The resource name of the reseller's
            account.
        page_size (int):
            Requested page size. Server might return
            fewer results than requested. If unspecified, at
            most 100 Offers will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            A token identifying a page of results, if other than the
            first one. Typically obtained via
            [ListTransferableOffersResponse.next_page_token][google.cloud.channel.v1.ListTransferableOffersResponse.next_page_token]
            of the previous
            [CloudChannelService.ListTransferableOffers][google.cloud.channel.v1.CloudChannelService.ListTransferableOffers]
            call.
        sku (str):
            Required. SKU for which the Offers are being
            looked up.
        language_code (str):
            The BCP-47 language code, such as "en-US".
            If specified, the response will be localized to
            the corresponding language code. Default is "en-
            US".
    """

    cloud_identity_id = proto.Field(
        proto.STRING, number=4, oneof="transferred_customer_identity"
    )

    customer_name = proto.Field(
        proto.STRING, number=5, oneof="transferred_customer_identity"
    )

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)

    sku = proto.Field(proto.STRING, number=6)

    language_code = proto.Field(proto.STRING, number=7)


class ListTransferableOffersResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListTransferableOffers][google.cloud.channel.v1.CloudChannelService.ListTransferableOffers].

    Attributes:
        transferable_offers (Sequence[google.cloud.channel_v1.types.TransferableOffer]):
            Information about Offers for a customer that
            can be used for transfer.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListTransferableOffersRequest.page_token][google.cloud.channel.v1.ListTransferableOffersRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    transferable_offers = proto.RepeatedField(
        proto.MESSAGE, number=1, message="TransferableOffer",
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class TransferableOffer(proto.Message):
    r"""TransferableOffer represents an Offer that can be used in
    Transfer. Read-only.

    Attributes:
        offer (google.cloud.channel_v1.types.Offer):
            Offer with parameter constraints updated to
            allow the Transfer.
    """

    offer = proto.Field(proto.MESSAGE, number=1, message=gcc_offers.Offer,)


class GetEntitlementRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.GetEntitlement][google.cloud.channel.v1.CloudChannelService.GetEntitlement].

    Attributes:
        name (str):
            Required. The resource name of the entitlement to retrieve.
            The name takes the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{id}
    """

    name = proto.Field(proto.STRING, number=1)


class ListChannelPartnerLinksRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListChannelPartnerLinks][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerLinks]

    Attributes:
        parent (str):
            Required. The resource name of the reseller account for
            listing channel partner links. The parent takes the format:
            accounts/{account_id}
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, server will pick a default size
            (25). The maximum value is 200, values above 200
            will be coerced to 200.
        page_token (str):
            Optional. A token identifying a page of results, if other
            than the first one. Typically obtained via
            [ListChannelPartnerLinksResponse.next_page_token][google.cloud.channel.v1.ListChannelPartnerLinksResponse.next_page_token]
            of the previous
            [CloudChannelService.ListChannelPartnerLinks][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerLinks]
            call.
        view (google.cloud.channel_v1.types.ChannelPartnerLinkView):
            Optional. The level of granularity the
            ChannelPartnerLink will display.
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)

    view = proto.Field(
        proto.ENUM, number=4, enum=gcc_channel_partner_links.ChannelPartnerLinkView,
    )


class ListChannelPartnerLinksResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListChannelPartnerLinks][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerLinks].

    Attributes:
        channel_partner_links (Sequence[google.cloud.channel_v1.types.ChannelPartnerLink]):
            The Channel partner links for a reseller.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListChannelPartnerLinksRequest.page_token][google.cloud.channel.v1.ListChannelPartnerLinksRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    channel_partner_links = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gcc_channel_partner_links.ChannelPartnerLink,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class GetChannelPartnerLinkRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.GetChannelPartnerLink][google.cloud.channel.v1.CloudChannelService.GetChannelPartnerLink].

    Attributes:
        name (str):
            Required. The resource name of the channel partner link to
            retrieve. The name takes the format:
            accounts/{account_id}/channelPartnerLinks/{id} where {id} is
            the Cloud Identity ID of the partner.
        view (google.cloud.channel_v1.types.ChannelPartnerLinkView):
            Optional. The level of granularity the
            ChannelPartnerLink will display.
    """

    name = proto.Field(proto.STRING, number=1)

    view = proto.Field(
        proto.ENUM, number=2, enum=gcc_channel_partner_links.ChannelPartnerLinkView,
    )


class CreateChannelPartnerLinkRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CreateChannelPartnerLink][google.cloud.channel.v1.CloudChannelService.CreateChannelPartnerLink]

    Attributes:
        parent (str):
            Required. The resource name of reseller's account for which
            to create a channel partner link. The parent takes the
            format: accounts/{account_id}
        channel_partner_link (google.cloud.channel_v1.types.ChannelPartnerLink):
            Required. The channel partner link to create. Either
            channel_partner_link.reseller_cloud_identity_id or domain
            can be used to create a link.
        domain (str):
            Optional. The invited partner's domain. Either domain or
            channel_partner_link.reseller_cloud_identity_id can be used
            to create a link.
    """

    parent = proto.Field(proto.STRING, number=1)

    channel_partner_link = proto.Field(
        proto.MESSAGE, number=2, message=gcc_channel_partner_links.ChannelPartnerLink,
    )

    domain = proto.Field(proto.STRING, number=3)


class UpdateChannelPartnerLinkRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.UpdateChannelPartnerLink][google.cloud.channel.v1.CloudChannelService.UpdateChannelPartnerLink]

    Attributes:
        name (str):
            Required. The resource name of the channel partner link to
            cancel. The name takes the format:
            accounts/{account_id}/channelPartnerLinks/{id} where {id} is
            the Cloud Identity ID of the partner.
        channel_partner_link (google.cloud.channel_v1.types.ChannelPartnerLink):
            Required. The channel partner link to update. Only field
            channel_partner_link.link_state is allowed to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask that applies to the resource. The
            only allowable value for update mask is
            channel_partner_link.link_state.
    """

    name = proto.Field(proto.STRING, number=1)

    channel_partner_link = proto.Field(
        proto.MESSAGE, number=2, message=gcc_channel_partner_links.ChannelPartnerLink,
    )

    update_mask = proto.Field(proto.MESSAGE, number=3, message=field_mask.FieldMask,)


class CreateEntitlementRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CreateEntitlement][google.cloud.channel.v1.CloudChannelService.CreateEntitlement]

    Attributes:
        parent (str):
            Required. The resource name of reseller's customer account
            in which to create the entitlement. The parent takes the
            format: accounts/{account_id}/customers/{customer_id}
        entitlement (google.cloud.channel_v1.types.Entitlement):
            Required. The entitlement to create.
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your
            request, the server will know to ignore the request if it
            has already been completed.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if the
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    parent = proto.Field(proto.STRING, number=1)

    entitlement = proto.Field(
        proto.MESSAGE, number=2, message=gcc_entitlements.Entitlement,
    )

    request_id = proto.Field(proto.STRING, number=5)


class TransferEntitlementsRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.TransferEntitlements][google.cloud.channel.v1.CloudChannelService.TransferEntitlements].

    Attributes:
        parent (str):
            Required. The resource name of reseller's customer account
            where the entitlements transfer to. The parent takes the
            format: accounts/{account_id}/customers/{customer_id}
        entitlements (Sequence[google.cloud.channel_v1.types.Entitlement]):
            Required. The new entitlements to be created
            or transferred.
        auth_token (str):
            This token is generated by the Super Admin of
            the resold customer to authorize a reseller to
            access their Cloud Identity and purchase
            entitlements on their behalf. This token can be
            omitted once the authorization is generated. See
            https://support.google.com/a/answer/7643790 for
            more details.
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your
            request, the server will know to ignore the request if it
            has already been completed.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if the
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    parent = proto.Field(proto.STRING, number=1)

    entitlements = proto.RepeatedField(
        proto.MESSAGE, number=2, message=gcc_entitlements.Entitlement,
    )

    auth_token = proto.Field(proto.STRING, number=4)

    request_id = proto.Field(proto.STRING, number=6)


class TransferEntitlementsResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.TransferEntitlements][google.cloud.channel.v1.CloudChannelService.TransferEntitlements].
    This will be put into the response field of
    google.longrunning.Operation.

    Attributes:
        entitlements (Sequence[google.cloud.channel_v1.types.Entitlement]):
            The entitlements that have been transferred.
    """

    entitlements = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gcc_entitlements.Entitlement,
    )


class TransferEntitlementsToGoogleRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.TransferEntitlementsToGoogle][google.cloud.channel.v1.CloudChannelService.TransferEntitlementsToGoogle].

    Attributes:
        parent (str):
            Required. The resource name of reseller's customer account
            where the entitlements transfer from. The parent takes the
            format: accounts/{account_id}/customers/{customer_id}
        entitlements (Sequence[google.cloud.channel_v1.types.Entitlement]):
            Required. The entitlements to be transferred
            to Google.
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your
            request, the server will know to ignore the request if it
            has already been completed.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if the
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    parent = proto.Field(proto.STRING, number=1)

    entitlements = proto.RepeatedField(
        proto.MESSAGE, number=2, message=gcc_entitlements.Entitlement,
    )

    request_id = proto.Field(proto.STRING, number=3)


class ChangeParametersRequest(proto.Message):
    r"""Request message for [CloudChannelService.ChangeParametersRequest][].

    Attributes:
        name (str):
            Required. The name of the entitlement to update. The name
            takes the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        parameters (Sequence[google.cloud.channel_v1.types.Parameter]):
            Required. Entitlement parameters to update.
            Only editable parameters are allowed to be
            changed.
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your
            request, the server will know to ignore the request if it
            has already been completed.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if the
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
        purchase_order_id (str):
            Optional. Purchase order ID provided by the
            reseller.
    """

    name = proto.Field(proto.STRING, number=1)

    parameters = proto.RepeatedField(
        proto.MESSAGE, number=2, message=gcc_entitlements.Parameter,
    )

    request_id = proto.Field(proto.STRING, number=4)

    purchase_order_id = proto.Field(proto.STRING, number=5)


class ChangeRenewalSettingsRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ChangeRenewalSettings][google.cloud.channel.v1.CloudChannelService.ChangeRenewalSettings].

    Attributes:
        name (str):
            Required. The name of the entitlement to update. The name
            takes the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        renewal_settings (google.cloud.channel_v1.types.RenewalSettings):
            Required. New renewal settings.
        request_id (str):
            Optional. A request ID to identify requests. Specify a
            unique request ID so that if you must retry your request,
            the server will know to ignore the request if it has already
            been completed.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if the
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name = proto.Field(proto.STRING, number=1)

    renewal_settings = proto.Field(
        proto.MESSAGE, number=4, message=gcc_entitlements.RenewalSettings,
    )

    request_id = proto.Field(proto.STRING, number=5)


class ChangeOfferRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ChangeOffer][google.cloud.channel.v1.CloudChannelService.ChangeOffer].

    Attributes:
        name (str):
            Required. The name of the entitlement to update. Format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        offer (str):
            Required. New Offer. Format:
            accounts/{account_id}/offers/{offer_id}.
        parameters (Sequence[google.cloud.channel_v1.types.Parameter]):
            Optional. Parameters needed to purchase the
            Offer.
        purchase_order_id (str):
            Optional. Purchase order id provided by the
            reseller.
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your
            request, the server will know to ignore the request if it
            has already been completed.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if the
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name = proto.Field(proto.STRING, number=1)

    offer = proto.Field(proto.STRING, number=2)

    parameters = proto.RepeatedField(
        proto.MESSAGE, number=3, message=gcc_entitlements.Parameter,
    )

    purchase_order_id = proto.Field(proto.STRING, number=5)

    request_id = proto.Field(proto.STRING, number=6)


class StartPaidServiceRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.StartPaidService][google.cloud.channel.v1.CloudChannelService.StartPaidService].

    Attributes:
        name (str):
            Required. The name of the entitlement for which paid service
            is being started. The name takes the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your
            request, the server will know to ignore the request if it
            has already been completed.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if the
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name = proto.Field(proto.STRING, number=1)

    request_id = proto.Field(proto.STRING, number=3)


class CancelEntitlementRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CancelEntitlement][google.cloud.channel.v1.CloudChannelService.CancelEntitlement].

    Attributes:
        name (str):
            Required. The resource name of the entitlement to cancel.
            The name takes the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your
            request, the server will know to ignore the request if it
            has already been completed.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if the
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name = proto.Field(proto.STRING, number=1)

    request_id = proto.Field(proto.STRING, number=3)


class SuspendEntitlementRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.SuspendEntitlement][google.cloud.channel.v1.CloudChannelService.SuspendEntitlement].

    Attributes:
        name (str):
            Required. The resource name of the entitlement to suspend.
            The name takes the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your
            request, the server will know to ignore the request if it
            has already been completed.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if the
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name = proto.Field(proto.STRING, number=1)

    request_id = proto.Field(proto.STRING, number=3)


class ActivateEntitlementRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ActivateEntitlement][google.cloud.channel.v1.CloudChannelService.ActivateEntitlement].

    Attributes:
        name (str):
            Required. The resource name of the entitlement to activate.
            The name takes the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        request_id (str):
            Optional. An optional request ID to identify requests.
            Specify a unique request ID so that if you must retry your
            request, the server will know to ignore the request if it
            has already been completed.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if the
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name = proto.Field(proto.STRING, number=1)

    request_id = proto.Field(proto.STRING, number=3)


class ListProductsRequest(proto.Message):
    r"""Request message for ListProducts.

    Attributes:
        account (str):
            Required. The resource name of the reseller account. Format:
            accounts/{account_id}.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, at most 100 Products will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results, if other than the first one.
        language_code (str):
            Optional. The BCP-47 language code, such as
            "en-US".  If specified, the response will be
            localized to the corresponding language code.
            Default is "en-US".
    """

    account = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)

    language_code = proto.Field(proto.STRING, number=4)


class ListProductsResponse(proto.Message):
    r"""Response message for ListProducts.

    Attributes:
        products (Sequence[google.cloud.channel_v1.types.Product]):
            List of Products requested.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    products = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gcc_products.Product,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class ListSkusRequest(proto.Message):
    r"""Request message for ListSkus.

    Attributes:
        parent (str):
            Required. The resource name of the Product for which to list
            SKUs. The parent takes the format: products/{product_id}.
            Supports products/- to retrieve SKUs for all products.
        account (str):
            Required. Resource name of the reseller. Format:
            accounts/{account_id}.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, at most 100 SKUs will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results, if other than the first one. Optional.
        language_code (str):
            Optional. The BCP-47 language code, such as
            "en-US".  If specified, the response will be
            localized to the corresponding language code.
            Default is "en-US".
    """

    parent = proto.Field(proto.STRING, number=1)

    account = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)

    language_code = proto.Field(proto.STRING, number=5)


class ListSkusResponse(proto.Message):
    r"""Response message for ListSkus.

    Attributes:
        skus (Sequence[google.cloud.channel_v1.types.Sku]):
            The list of SKUs requested.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    skus = proto.RepeatedField(proto.MESSAGE, number=1, message=gcc_products.Sku,)

    next_page_token = proto.Field(proto.STRING, number=2)


class ListOffersRequest(proto.Message):
    r"""Request message for ListOffers.

    Attributes:
        parent (str):
            Required. The resource name of the reseller account from
            which to list Offers. The parent takes the format:
            accounts/{account_id}.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, at most 500 Offers will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results, if other than the first one.
        filter (str):
            Optional. The expression to filter results by
            name (name of the Offer), sku.name (name of the
            SKU) or sku.product.name (name of the Product).
            Example 1: sku.product.name=products/p1 AND
            sku.name!=products/p1/skus/s1 Example 2:
            name=accounts/a1/offers/o1
        language_code (str):
            Optional. The BCP-47 language code, such as
            "en-US".  If specified, the response will be
            localized to the corresponding language code.
            Default is "en-US".
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)

    filter = proto.Field(proto.STRING, number=4)

    language_code = proto.Field(proto.STRING, number=5)


class ListOffersResponse(proto.Message):
    r"""Response message for ListOffers.

    Attributes:
        offers (Sequence[google.cloud.channel_v1.types.Offer]):
            The list of Offers requested.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    offers = proto.RepeatedField(proto.MESSAGE, number=1, message=gcc_offers.Offer,)

    next_page_token = proto.Field(proto.STRING, number=2)


class ListPurchasableSkusRequest(proto.Message):
    r"""Request message for ListPurchasableSkus.

    Attributes:
        create_entitlement_purchase (google.cloud.channel_v1.types.ListPurchasableSkusRequest.CreateEntitlementPurchase):
            List SKUs for CreateEntitlement purchase.
        change_offer_purchase (google.cloud.channel_v1.types.ListPurchasableSkusRequest.ChangeOfferPurchase):
            List SKUs for ChangeOffer purchase with a new
            SKU.
        customer (str):
            Required. The resource name of the customer for which to
            list SKUs. Format:
            accounts/{account_id}/customers/{customer_id}.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, at most 100 SKUs will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results, if other than the first one.
        language_code (str):
            Optional. The BCP-47 language code, such as
            "en-US".  If specified, the response will be
            localized to the corresponding language code.
            Default is "en-US".
    """

    class CreateEntitlementPurchase(proto.Message):
        r"""List SKUs for a new entitlement. Make the purchase using
        [CloudChannelService.CreateEntitlement][google.cloud.channel.v1.CloudChannelService.CreateEntitlement].

        Attributes:
            product (str):
                Required. List SKUs belonging to this Product. Format:
                products/{product_id}. Supports products/- to retrieve SKUs
                for all products.
        """

        product = proto.Field(proto.STRING, number=1)

    class ChangeOfferPurchase(proto.Message):
        r"""List SKUs for upgrading or downgrading an entitlement. Make the
        purchase using
        [CloudChannelService.ChangeOffer][google.cloud.channel.v1.CloudChannelService.ChangeOffer].

        Attributes:
            entitlement (str):
                Required. Resource name of the entitlement. Format:
                accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
            change_type (google.cloud.channel_v1.types.ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType):
                Required. Change Type for the entitlement.
        """

        class ChangeType(proto.Enum):
            r"""Change Type enum."""
            CHANGE_TYPE_UNSPECIFIED = 0
            UPGRADE = 1
            DOWNGRADE = 2

        entitlement = proto.Field(proto.STRING, number=1)

        change_type = proto.Field(
            proto.ENUM,
            number=2,
            enum="ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType",
        )

    create_entitlement_purchase = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="purchase_option",
        message=CreateEntitlementPurchase,
    )

    change_offer_purchase = proto.Field(
        proto.MESSAGE, number=3, oneof="purchase_option", message=ChangeOfferPurchase,
    )

    customer = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=4)

    page_token = proto.Field(proto.STRING, number=5)

    language_code = proto.Field(proto.STRING, number=6)


class ListPurchasableSkusResponse(proto.Message):
    r"""Response message for ListPurchasableSkus.

    Attributes:
        purchasable_skus (Sequence[google.cloud.channel_v1.types.PurchasableSku]):
            The list of SKUs requested.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    purchasable_skus = proto.RepeatedField(
        proto.MESSAGE, number=1, message="PurchasableSku",
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class PurchasableSku(proto.Message):
    r"""SKU that can be used for a puchase. This is used in
    ListPurchasableSku API response.

    Attributes:
        sku (google.cloud.channel_v1.types.Sku):
            SKU
    """

    sku = proto.Field(proto.MESSAGE, number=1, message=gcc_products.Sku,)


class ListPurchasableOffersRequest(proto.Message):
    r"""Request message for ListPurchasableOffers.

    Attributes:
        create_entitlement_purchase (google.cloud.channel_v1.types.ListPurchasableOffersRequest.CreateEntitlementPurchase):
            List Offers for CreateEntitlement purchase.
        change_offer_purchase (google.cloud.channel_v1.types.ListPurchasableOffersRequest.ChangeOfferPurchase):
            List Offers for ChangeOffer purchase.
        customer (str):
            Required. The resource name of the customer for which to
            list Offers. Format:
            accounts/{account_id}/customers/{customer_id}.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, at most 100 Offers will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results, if other than the first one.
        language_code (str):
            Optional. The BCP-47 language code, such as
            "en-US".  If specified, the response will be
            localized to the corresponding language code.
            Default is "en-US".
    """

    class CreateEntitlementPurchase(proto.Message):
        r"""List Offers for CreateEntitlement purchase.

        Attributes:
            sku (str):
                Required. SKU that the result should be restricted to.
                Format: products/{product_id}/skus/{sku_id}.
        """

        sku = proto.Field(proto.STRING, number=1)

    class ChangeOfferPurchase(proto.Message):
        r"""List Offers for ChangeOffer purchase.

        Attributes:
            entitlement (str):
                Required. Resource name of the entitlement. Format:
                accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
            new_sku (str):
                Optional. Resource name of the SKU that is being changed to.
                Should be provided if upgrading or downgrading an
                entitlement. Format: products/{product_id}/skus/{sku_id}
        """

        entitlement = proto.Field(proto.STRING, number=1)

        new_sku = proto.Field(proto.STRING, number=2)

    create_entitlement_purchase = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="purchase_option",
        message=CreateEntitlementPurchase,
    )

    change_offer_purchase = proto.Field(
        proto.MESSAGE, number=3, oneof="purchase_option", message=ChangeOfferPurchase,
    )

    customer = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=4)

    page_token = proto.Field(proto.STRING, number=5)

    language_code = proto.Field(proto.STRING, number=6)


class ListPurchasableOffersResponse(proto.Message):
    r"""Response message for ListPurchasableOffers.

    Attributes:
        purchasable_offers (Sequence[google.cloud.channel_v1.types.PurchasableOffer]):
            The list of Offers requested.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    purchasable_offers = proto.RepeatedField(
        proto.MESSAGE, number=1, message="PurchasableOffer",
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class PurchasableOffer(proto.Message):
    r"""Offer that can be puchased for a customer. This is used in
    ListPurchasableOffer API response.

    Attributes:
        offer (google.cloud.channel_v1.types.Offer):
            Offer.
    """

    offer = proto.Field(proto.MESSAGE, number=1, message=gcc_offers.Offer,)


__all__ = tuple(sorted(__protobuf__.manifest))
