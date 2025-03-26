// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetPuppetclass(ctx *pulumi.Context, args *GetPuppetclassArgs, opts ...pulumi.InvokeOption) (*GetPuppetclassResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetPuppetclassResult
	err := ctx.Invoke("foreman:index/getPuppetclass:getPuppetclass", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPuppetclass.
type GetPuppetclassArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getPuppetclass.
type GetPuppetclassResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
}

func GetPuppetclassOutput(ctx *pulumi.Context, args GetPuppetclassOutputArgs, opts ...pulumi.InvokeOption) GetPuppetclassResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetPuppetclassResultOutput, error) {
			args := v.(GetPuppetclassArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("foreman:index/getPuppetclass:getPuppetclass", args, GetPuppetclassResultOutput{}, options).(GetPuppetclassResultOutput), nil
		}).(GetPuppetclassResultOutput)
}

// A collection of arguments for invoking getPuppetclass.
type GetPuppetclassOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (GetPuppetclassOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPuppetclassArgs)(nil)).Elem()
}

// A collection of values returned by getPuppetclass.
type GetPuppetclassResultOutput struct{ *pulumi.OutputState }

func (GetPuppetclassResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPuppetclassResult)(nil)).Elem()
}

func (o GetPuppetclassResultOutput) ToGetPuppetclassResultOutput() GetPuppetclassResultOutput {
	return o
}

func (o GetPuppetclassResultOutput) ToGetPuppetclassResultOutputWithContext(ctx context.Context) GetPuppetclassResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetPuppetclassResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetPuppetclassResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetPuppetclassResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetPuppetclassResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetPuppetclassResultOutput{})
}
