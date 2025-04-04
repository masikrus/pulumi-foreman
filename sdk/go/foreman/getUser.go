// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package foreman

import (
	"context"
	"reflect"

	"github.com/masikrus/pulumi-foreman/sdk/go/foreman/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupUser(ctx *pulumi.Context, args *LookupUserArgs, opts ...pulumi.InvokeOption) (*LookupUserResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupUserResult
	err := ctx.Invoke("foreman:index/getUser:getUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUser.
type LookupUserArgs struct {
	Description *string `pulumi:"description"`
	Firstname   *string `pulumi:"firstname"`
	Lastname    *string `pulumi:"lastname"`
	Login       *string `pulumi:"login"`
	Mail        *string `pulumi:"mail"`
}

// A collection of values returned by getUser.
type LookupUserResult struct {
	Admin                 bool    `pulumi:"admin"`
	AuthSourceId          int     `pulumi:"authSourceId"`
	DefaultLocationId     int     `pulumi:"defaultLocationId"`
	DefaultOrganizationId int     `pulumi:"defaultOrganizationId"`
	Description           *string `pulumi:"description"`
	Firstname             *string `pulumi:"firstname"`
	// The provider-assigned unique ID for this managed resource.
	Id              string  `pulumi:"id"`
	Lastname        *string `pulumi:"lastname"`
	Locale          string  `pulumi:"locale"`
	LocationIds     []int   `pulumi:"locationIds"`
	Login           *string `pulumi:"login"`
	Mail            *string `pulumi:"mail"`
	OrganizationIds []int   `pulumi:"organizationIds"`
	Password        string  `pulumi:"password"`
}

func LookupUserOutput(ctx *pulumi.Context, args LookupUserOutputArgs, opts ...pulumi.InvokeOption) LookupUserResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupUserResultOutput, error) {
			args := v.(LookupUserArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("foreman:index/getUser:getUser", args, LookupUserResultOutput{}, options).(LookupUserResultOutput), nil
		}).(LookupUserResultOutput)
}

// A collection of arguments for invoking getUser.
type LookupUserOutputArgs struct {
	Description pulumi.StringPtrInput `pulumi:"description"`
	Firstname   pulumi.StringPtrInput `pulumi:"firstname"`
	Lastname    pulumi.StringPtrInput `pulumi:"lastname"`
	Login       pulumi.StringPtrInput `pulumi:"login"`
	Mail        pulumi.StringPtrInput `pulumi:"mail"`
}

func (LookupUserOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUserArgs)(nil)).Elem()
}

// A collection of values returned by getUser.
type LookupUserResultOutput struct{ *pulumi.OutputState }

func (LookupUserResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUserResult)(nil)).Elem()
}

func (o LookupUserResultOutput) ToLookupUserResultOutput() LookupUserResultOutput {
	return o
}

func (o LookupUserResultOutput) ToLookupUserResultOutputWithContext(ctx context.Context) LookupUserResultOutput {
	return o
}

func (o LookupUserResultOutput) Admin() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupUserResult) bool { return v.Admin }).(pulumi.BoolOutput)
}

func (o LookupUserResultOutput) AuthSourceId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupUserResult) int { return v.AuthSourceId }).(pulumi.IntOutput)
}

func (o LookupUserResultOutput) DefaultLocationId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupUserResult) int { return v.DefaultLocationId }).(pulumi.IntOutput)
}

func (o LookupUserResultOutput) DefaultOrganizationId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupUserResult) int { return v.DefaultOrganizationId }).(pulumi.IntOutput)
}

func (o LookupUserResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupUserResultOutput) Firstname() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Firstname }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupUserResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUserResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupUserResultOutput) Lastname() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Lastname }).(pulumi.StringPtrOutput)
}

func (o LookupUserResultOutput) Locale() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUserResult) string { return v.Locale }).(pulumi.StringOutput)
}

func (o LookupUserResultOutput) LocationIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v LookupUserResult) []int { return v.LocationIds }).(pulumi.IntArrayOutput)
}

func (o LookupUserResultOutput) Login() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Login }).(pulumi.StringPtrOutput)
}

func (o LookupUserResultOutput) Mail() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Mail }).(pulumi.StringPtrOutput)
}

func (o LookupUserResultOutput) OrganizationIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v LookupUserResult) []int { return v.OrganizationIds }).(pulumi.IntArrayOutput)
}

func (o LookupUserResultOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUserResult) string { return v.Password }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupUserResultOutput{})
}
