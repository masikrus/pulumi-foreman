// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupUsergroup(ctx *pulumi.Context, args *LookupUsergroupArgs, opts ...pulumi.InvokeOption) (*LookupUsergroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupUsergroupResult
	err := ctx.Invoke("foreman:index/getUsergroup:getUsergroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUsergroup.
type LookupUsergroupArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getUsergroup.
type LookupUsergroupResult struct {
	Admin bool `pulumi:"admin"`
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
}

func LookupUsergroupOutput(ctx *pulumi.Context, args LookupUsergroupOutputArgs, opts ...pulumi.InvokeOption) LookupUsergroupResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupUsergroupResultOutput, error) {
			args := v.(LookupUsergroupArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("foreman:index/getUsergroup:getUsergroup", args, LookupUsergroupResultOutput{}, options).(LookupUsergroupResultOutput), nil
		}).(LookupUsergroupResultOutput)
}

// A collection of arguments for invoking getUsergroup.
type LookupUsergroupOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupUsergroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUsergroupArgs)(nil)).Elem()
}

// A collection of values returned by getUsergroup.
type LookupUsergroupResultOutput struct{ *pulumi.OutputState }

func (LookupUsergroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUsergroupResult)(nil)).Elem()
}

func (o LookupUsergroupResultOutput) ToLookupUsergroupResultOutput() LookupUsergroupResultOutput {
	return o
}

func (o LookupUsergroupResultOutput) ToLookupUsergroupResultOutputWithContext(ctx context.Context) LookupUsergroupResultOutput {
	return o
}

func (o LookupUsergroupResultOutput) Admin() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupUsergroupResult) bool { return v.Admin }).(pulumi.BoolOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupUsergroupResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUsergroupResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupUsergroupResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUsergroupResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupUsergroupResultOutput{})
}
