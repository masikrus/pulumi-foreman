// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupArchitecture(ctx *pulumi.Context, args *LookupArchitectureArgs, opts ...pulumi.InvokeOption) (*LookupArchitectureResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupArchitectureResult
	err := ctx.Invoke("foreman:index/getArchitecture:getArchitecture", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getArchitecture.
type LookupArchitectureArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getArchitecture.
type LookupArchitectureResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id                 string `pulumi:"id"`
	Name               string `pulumi:"name"`
	OperatingsystemIds []int  `pulumi:"operatingsystemIds"`
}

func LookupArchitectureOutput(ctx *pulumi.Context, args LookupArchitectureOutputArgs, opts ...pulumi.InvokeOption) LookupArchitectureResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupArchitectureResultOutput, error) {
			args := v.(LookupArchitectureArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("foreman:index/getArchitecture:getArchitecture", args, LookupArchitectureResultOutput{}, options).(LookupArchitectureResultOutput), nil
		}).(LookupArchitectureResultOutput)
}

// A collection of arguments for invoking getArchitecture.
type LookupArchitectureOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupArchitectureOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupArchitectureArgs)(nil)).Elem()
}

// A collection of values returned by getArchitecture.
type LookupArchitectureResultOutput struct{ *pulumi.OutputState }

func (LookupArchitectureResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupArchitectureResult)(nil)).Elem()
}

func (o LookupArchitectureResultOutput) ToLookupArchitectureResultOutput() LookupArchitectureResultOutput {
	return o
}

func (o LookupArchitectureResultOutput) ToLookupArchitectureResultOutputWithContext(ctx context.Context) LookupArchitectureResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o LookupArchitectureResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupArchitectureResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupArchitectureResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupArchitectureResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupArchitectureResultOutput) OperatingsystemIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v LookupArchitectureResult) []int { return v.OperatingsystemIds }).(pulumi.IntArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupArchitectureResultOutput{})
}
