// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupKatelloRepository(ctx *pulumi.Context, args *LookupKatelloRepositoryArgs, opts ...pulumi.InvokeOption) (*LookupKatelloRepositoryResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupKatelloRepositoryResult
	err := ctx.Invoke("foreman:index/getKatelloRepository:getKatelloRepository", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getKatelloRepository.
type LookupKatelloRepositoryArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getKatelloRepository.
type LookupKatelloRepositoryResult struct {
	AnsibleCollectionRequirements string `pulumi:"ansibleCollectionRequirements"`
	ChecksumType                  string `pulumi:"checksumType"`
	ContentType                   string `pulumi:"contentType"`
	DebArchitectures              string `pulumi:"debArchitectures"`
	DebComponents                 string `pulumi:"debComponents"`
	DebReleases                   string `pulumi:"debReleases"`
	Description                   string `pulumi:"description"`
	DockerTagsWhitelist           string `pulumi:"dockerTagsWhitelist"`
	DockerUpstreamName            string `pulumi:"dockerUpstreamName"`
	DownloadConcurrency           int    `pulumi:"downloadConcurrency"`
	DownloadPolicy                string `pulumi:"downloadPolicy"`
	GpgKeyId                      int    `pulumi:"gpgKeyId"`
	HttpProxyId                   int    `pulumi:"httpProxyId"`
	HttpProxyPolicy               string `pulumi:"httpProxyPolicy"`
	// The provider-assigned unique ID for this managed resource.
	Id                string `pulumi:"id"`
	IgnorableContent  string `pulumi:"ignorableContent"`
	IgnoreGlobalProxy bool   `pulumi:"ignoreGlobalProxy"`
	Label             string `pulumi:"label"`
	MirrorOnSync      bool   `pulumi:"mirrorOnSync"`
	MirroringPolicy   string `pulumi:"mirroringPolicy"`
	Name              string `pulumi:"name"`
	ProductId         int    `pulumi:"productId"`
	Unprotected       bool   `pulumi:"unprotected"`
	UpstreamPassword  string `pulumi:"upstreamPassword"`
	UpstreamUsername  string `pulumi:"upstreamUsername"`
	Url               string `pulumi:"url"`
	VerifySslOnSync   bool   `pulumi:"verifySslOnSync"`
}

func LookupKatelloRepositoryOutput(ctx *pulumi.Context, args LookupKatelloRepositoryOutputArgs, opts ...pulumi.InvokeOption) LookupKatelloRepositoryResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupKatelloRepositoryResultOutput, error) {
			args := v.(LookupKatelloRepositoryArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("foreman:index/getKatelloRepository:getKatelloRepository", args, LookupKatelloRepositoryResultOutput{}, options).(LookupKatelloRepositoryResultOutput), nil
		}).(LookupKatelloRepositoryResultOutput)
}

// A collection of arguments for invoking getKatelloRepository.
type LookupKatelloRepositoryOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupKatelloRepositoryOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKatelloRepositoryArgs)(nil)).Elem()
}

// A collection of values returned by getKatelloRepository.
type LookupKatelloRepositoryResultOutput struct{ *pulumi.OutputState }

func (LookupKatelloRepositoryResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKatelloRepositoryResult)(nil)).Elem()
}

func (o LookupKatelloRepositoryResultOutput) ToLookupKatelloRepositoryResultOutput() LookupKatelloRepositoryResultOutput {
	return o
}

func (o LookupKatelloRepositoryResultOutput) ToLookupKatelloRepositoryResultOutputWithContext(ctx context.Context) LookupKatelloRepositoryResultOutput {
	return o
}

func (o LookupKatelloRepositoryResultOutput) AnsibleCollectionRequirements() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.AnsibleCollectionRequirements }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) ChecksumType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.ChecksumType }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) ContentType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.ContentType }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) DebArchitectures() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.DebArchitectures }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) DebComponents() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.DebComponents }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) DebReleases() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.DebReleases }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) DockerTagsWhitelist() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.DockerTagsWhitelist }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) DockerUpstreamName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.DockerUpstreamName }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) DownloadConcurrency() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) int { return v.DownloadConcurrency }).(pulumi.IntOutput)
}

func (o LookupKatelloRepositoryResultOutput) DownloadPolicy() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.DownloadPolicy }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) GpgKeyId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) int { return v.GpgKeyId }).(pulumi.IntOutput)
}

func (o LookupKatelloRepositoryResultOutput) HttpProxyId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) int { return v.HttpProxyId }).(pulumi.IntOutput)
}

func (o LookupKatelloRepositoryResultOutput) HttpProxyPolicy() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.HttpProxyPolicy }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupKatelloRepositoryResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) IgnorableContent() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.IgnorableContent }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) IgnoreGlobalProxy() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) bool { return v.IgnoreGlobalProxy }).(pulumi.BoolOutput)
}

func (o LookupKatelloRepositoryResultOutput) Label() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.Label }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) MirrorOnSync() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) bool { return v.MirrorOnSync }).(pulumi.BoolOutput)
}

func (o LookupKatelloRepositoryResultOutput) MirroringPolicy() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.MirroringPolicy }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) ProductId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) int { return v.ProductId }).(pulumi.IntOutput)
}

func (o LookupKatelloRepositoryResultOutput) Unprotected() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) bool { return v.Unprotected }).(pulumi.BoolOutput)
}

func (o LookupKatelloRepositoryResultOutput) UpstreamPassword() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.UpstreamPassword }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) UpstreamUsername() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.UpstreamUsername }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) string { return v.Url }).(pulumi.StringOutput)
}

func (o LookupKatelloRepositoryResultOutput) VerifySslOnSync() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupKatelloRepositoryResult) bool { return v.VerifySslOnSync }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupKatelloRepositoryResultOutput{})
}
