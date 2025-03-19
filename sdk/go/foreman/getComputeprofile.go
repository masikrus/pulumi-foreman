// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupComputeprofile(ctx *pulumi.Context, args *LookupComputeprofileArgs, opts ...pulumi.InvokeOption) (*LookupComputeprofileResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupComputeprofileResult
	err := ctx.Invoke("foreman:index/getComputeprofile:getComputeprofile", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getComputeprofile.
type LookupComputeprofileArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getComputeprofile.
type LookupComputeprofileResult struct {
	__meta_           bool                                `pulumi:"__meta_"`
	ComputeAttributes []GetComputeprofileComputeAttribute `pulumi:"computeAttributes"`
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
}

func LookupComputeprofileOutput(ctx *pulumi.Context, args LookupComputeprofileOutputArgs, opts ...pulumi.InvokeOption) LookupComputeprofileResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupComputeprofileResultOutput, error) {
			args := v.(LookupComputeprofileArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("foreman:index/getComputeprofile:getComputeprofile", args, LookupComputeprofileResultOutput{}, options).(LookupComputeprofileResultOutput), nil
		}).(LookupComputeprofileResultOutput)
}

// A collection of arguments for invoking getComputeprofile.
type LookupComputeprofileOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupComputeprofileOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupComputeprofileArgs)(nil)).Elem()
}

// A collection of values returned by getComputeprofile.
type LookupComputeprofileResultOutput struct{ *pulumi.OutputState }

func (LookupComputeprofileResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupComputeprofileResult)(nil)).Elem()
}

func (o LookupComputeprofileResultOutput) ToLookupComputeprofileResultOutput() LookupComputeprofileResultOutput {
	return o
}

func (o LookupComputeprofileResultOutput) ToLookupComputeprofileResultOutputWithContext(ctx context.Context) LookupComputeprofileResultOutput {
	return o
}

func (o LookupComputeprofileResultOutput) __meta_() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupComputeprofileResult) bool { return v.__meta_ }).(pulumi.BoolOutput)
}

func (o LookupComputeprofileResultOutput) ComputeAttributes() GetComputeprofileComputeAttributeArrayOutput {
	return o.ApplyT(func(v LookupComputeprofileResult) []GetComputeprofileComputeAttribute { return v.ComputeAttributes }).(GetComputeprofileComputeAttributeArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupComputeprofileResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupComputeprofileResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupComputeprofileResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupComputeprofileResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupComputeprofileResultOutput{})
}
