// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"errors"
	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The provider type for the foreman package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	// The username to authenticate against Foreman. This can also be set through the environment variable
	// `FOREMAN_CLIENT_PASSWORD`. Defaults to `""`.
	ClientPassword pulumi.StringPtrOutput `pulumi:"clientPassword"`
	// The username to authenticate against Foreman. This can also be set through the environment variable
	// `FOREMAN_CLIENT_USERNAME`. Defaults to `""`.
	ClientUsername  pulumi.StringPtrOutput `pulumi:"clientUsername"`
	ProviderLogfile pulumi.StringPtrOutput `pulumi:"providerLogfile"`
	// The level of verbosity for the provider's log file. This setting determines which types of log messages are written and
	// which are ignored. Possible values (from most verbose to least verbose) include 'DEBUG', 'TRACE', 'INFO', 'WARNING',
	// 'ERROR', and 'NONE'. The provider's logs will be written to the location specified by `providerLogfile`. This can also
	// be set through the environment variable `FOREMAN_PROVIDER_LOGLEVEL`. Defaults to `'INFO'`.
	ProviderLoglevel pulumi.StringPtrOutput `pulumi:"providerLoglevel"`
	// The hostname / IP address of the Foreman REST API server
	ServerHostname pulumi.StringOutput `pulumi:"serverHostname"`
	// The protocol the Foreman REST API server is using for communication. Defaults to `"https"`.
	ServerProtocol pulumi.StringPtrOutput `pulumi:"serverProtocol"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ServerHostname == nil {
		return nil, errors.New("invalid value for required argument 'ServerHostname'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:foreman", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// Whether or not the client should try to authenticate through the HTTP negotiate mechanism. Defaults to `false`.
	ClientAuthNegotiate *bool `pulumi:"clientAuthNegotiate"`
	// The username to authenticate against Foreman. This can also be set through the environment variable
	// `FOREMAN_CLIENT_PASSWORD`. Defaults to `""`.
	ClientPassword *string `pulumi:"clientPassword"`
	// Whether or not to verify the server's certificate. Defaults to `false`.
	ClientTlsInsecure *bool `pulumi:"clientTlsInsecure"`
	// The username to authenticate against Foreman. This can also be set through the environment variable
	// `FOREMAN_CLIENT_USERNAME`. Defaults to `""`.
	ClientUsername *string `pulumi:"clientUsername"`
	// The location for all resources requested and created by the providerDefaults to "0". Set organizationId and locationId
	// to a value < 0 if you need to disable Locations and Organizations on Foreman older than 1.21
	LocationId *int `pulumi:"locationId"`
	// The organization for all resource requested and created by the Provider Defaults to "0". Set organizationId and
	// locationId to a value < 0 if you need to disable Locations and Organizations on Foreman older than 1.21
	OrganizationId  *int    `pulumi:"organizationId"`
	ProviderLogfile *string `pulumi:"providerLogfile"`
	// The level of verbosity for the provider's log file. This setting determines which types of log messages are written and
	// which are ignored. Possible values (from most verbose to least verbose) include 'DEBUG', 'TRACE', 'INFO', 'WARNING',
	// 'ERROR', and 'NONE'. The provider's logs will be written to the location specified by `providerLogfile`. This can also
	// be set through the environment variable `FOREMAN_PROVIDER_LOGLEVEL`. Defaults to `'INFO'`.
	ProviderLoglevel *string `pulumi:"providerLoglevel"`
	// The hostname / IP address of the Foreman REST API server
	ServerHostname string `pulumi:"serverHostname"`
	// The protocol the Foreman REST API server is using for communication. Defaults to `"https"`.
	ServerProtocol *string `pulumi:"serverProtocol"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// Whether or not the client should try to authenticate through the HTTP negotiate mechanism. Defaults to `false`.
	ClientAuthNegotiate pulumi.BoolPtrInput
	// The username to authenticate against Foreman. This can also be set through the environment variable
	// `FOREMAN_CLIENT_PASSWORD`. Defaults to `""`.
	ClientPassword pulumi.StringPtrInput
	// Whether or not to verify the server's certificate. Defaults to `false`.
	ClientTlsInsecure pulumi.BoolPtrInput
	// The username to authenticate against Foreman. This can also be set through the environment variable
	// `FOREMAN_CLIENT_USERNAME`. Defaults to `""`.
	ClientUsername pulumi.StringPtrInput
	// The location for all resources requested and created by the providerDefaults to "0". Set organizationId and locationId
	// to a value < 0 if you need to disable Locations and Organizations on Foreman older than 1.21
	LocationId pulumi.IntPtrInput
	// The organization for all resource requested and created by the Provider Defaults to "0". Set organizationId and
	// locationId to a value < 0 if you need to disable Locations and Organizations on Foreman older than 1.21
	OrganizationId  pulumi.IntPtrInput
	ProviderLogfile pulumi.StringPtrInput
	// The level of verbosity for the provider's log file. This setting determines which types of log messages are written and
	// which are ignored. Possible values (from most verbose to least verbose) include 'DEBUG', 'TRACE', 'INFO', 'WARNING',
	// 'ERROR', and 'NONE'. The provider's logs will be written to the location specified by `providerLogfile`. This can also
	// be set through the environment variable `FOREMAN_PROVIDER_LOGLEVEL`. Defaults to `'INFO'`.
	ProviderLoglevel pulumi.StringPtrInput
	// The hostname / IP address of the Foreman REST API server
	ServerHostname pulumi.StringInput
	// The protocol the Foreman REST API server is using for communication. Defaults to `"https"`.
	ServerProtocol pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

// The username to authenticate against Foreman. This can also be set through the environment variable
// `FOREMAN_CLIENT_PASSWORD`. Defaults to `""`.
func (o ProviderOutput) ClientPassword() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ClientPassword }).(pulumi.StringPtrOutput)
}

// The username to authenticate against Foreman. This can also be set through the environment variable
// `FOREMAN_CLIENT_USERNAME`. Defaults to `""`.
func (o ProviderOutput) ClientUsername() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ClientUsername }).(pulumi.StringPtrOutput)
}

func (o ProviderOutput) ProviderLogfile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ProviderLogfile }).(pulumi.StringPtrOutput)
}

// The level of verbosity for the provider's log file. This setting determines which types of log messages are written and
// which are ignored. Possible values (from most verbose to least verbose) include 'DEBUG', 'TRACE', 'INFO', 'WARNING',
// 'ERROR', and 'NONE'. The provider's logs will be written to the location specified by `providerLogfile`. This can also
// be set through the environment variable `FOREMAN_PROVIDER_LOGLEVEL`. Defaults to `'INFO'`.
func (o ProviderOutput) ProviderLoglevel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ProviderLoglevel }).(pulumi.StringPtrOutput)
}

// The hostname / IP address of the Foreman REST API server
func (o ProviderOutput) ServerHostname() pulumi.StringOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringOutput { return v.ServerHostname }).(pulumi.StringOutput)
}

// The protocol the Foreman REST API server is using for communication. Defaults to `"https"`.
func (o ProviderOutput) ServerProtocol() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ServerProtocol }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}
