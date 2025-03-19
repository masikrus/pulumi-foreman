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

type Parameter struct {
	pulumi.CustomResourceState

	// @SUMMARY Foreman representation of parameter. Parameters serve as an identification string that defines autonomy,
	// authority, or control for a portion of a network.
	__meta_ pulumi.BoolOutput `pulumi:"__meta_"`
	// ID of the domain to assign this parameter to
	DomainId pulumi.IntPtrOutput `pulumi:"domainId"`
	// ID of the host to assign this parameter to
	HostId pulumi.IntPtrOutput `pulumi:"hostId"`
	// ID of the host group to assign this parameter to
	HostgroupId pulumi.IntPtrOutput `pulumi:"hostgroupId"`
	Name        pulumi.StringOutput `pulumi:"name"`
	// ID of the operating system to assign this parameter to
	OperatingsystemId pulumi.IntPtrOutput `pulumi:"operatingsystemId"`
	// ID of the subnet to assign this parameter to
	SubnetId pulumi.IntPtrOutput `pulumi:"subnetId"`
	Value    pulumi.StringOutput `pulumi:"value"`
}

// NewParameter registers a new resource with the given unique name, arguments, and options.
func NewParameter(ctx *pulumi.Context,
	name string, args *ParameterArgs, opts ...pulumi.ResourceOption) (*Parameter, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Parameter
	err := ctx.RegisterResource("foreman:index/parameter:Parameter", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetParameter gets an existing Parameter resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetParameter(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ParameterState, opts ...pulumi.ResourceOption) (*Parameter, error) {
	var resource Parameter
	err := ctx.ReadResource("foreman:index/parameter:Parameter", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Parameter resources.
type parameterState struct {
	// @SUMMARY Foreman representation of parameter. Parameters serve as an identification string that defines autonomy,
	// authority, or control for a portion of a network.
	__meta_ *bool `pulumi:"__meta_"`
	// ID of the domain to assign this parameter to
	DomainId *int `pulumi:"domainId"`
	// ID of the host to assign this parameter to
	HostId *int `pulumi:"hostId"`
	// ID of the host group to assign this parameter to
	HostgroupId *int    `pulumi:"hostgroupId"`
	Name        *string `pulumi:"name"`
	// ID of the operating system to assign this parameter to
	OperatingsystemId *int `pulumi:"operatingsystemId"`
	// ID of the subnet to assign this parameter to
	SubnetId *int    `pulumi:"subnetId"`
	Value    *string `pulumi:"value"`
}

type ParameterState struct {
	// @SUMMARY Foreman representation of parameter. Parameters serve as an identification string that defines autonomy,
	// authority, or control for a portion of a network.
	__meta_ pulumi.BoolPtrInput
	// ID of the domain to assign this parameter to
	DomainId pulumi.IntPtrInput
	// ID of the host to assign this parameter to
	HostId pulumi.IntPtrInput
	// ID of the host group to assign this parameter to
	HostgroupId pulumi.IntPtrInput
	Name        pulumi.StringPtrInput
	// ID of the operating system to assign this parameter to
	OperatingsystemId pulumi.IntPtrInput
	// ID of the subnet to assign this parameter to
	SubnetId pulumi.IntPtrInput
	Value    pulumi.StringPtrInput
}

func (ParameterState) ElementType() reflect.Type {
	return reflect.TypeOf((*parameterState)(nil)).Elem()
}

type parameterArgs struct {
	// ID of the domain to assign this parameter to
	DomainId *int `pulumi:"domainId"`
	// ID of the host to assign this parameter to
	HostId *int `pulumi:"hostId"`
	// ID of the host group to assign this parameter to
	HostgroupId *int    `pulumi:"hostgroupId"`
	Name        *string `pulumi:"name"`
	// ID of the operating system to assign this parameter to
	OperatingsystemId *int `pulumi:"operatingsystemId"`
	// ID of the subnet to assign this parameter to
	SubnetId *int   `pulumi:"subnetId"`
	Value    string `pulumi:"value"`
}

// The set of arguments for constructing a Parameter resource.
type ParameterArgs struct {
	// ID of the domain to assign this parameter to
	DomainId pulumi.IntPtrInput
	// ID of the host to assign this parameter to
	HostId pulumi.IntPtrInput
	// ID of the host group to assign this parameter to
	HostgroupId pulumi.IntPtrInput
	Name        pulumi.StringPtrInput
	// ID of the operating system to assign this parameter to
	OperatingsystemId pulumi.IntPtrInput
	// ID of the subnet to assign this parameter to
	SubnetId pulumi.IntPtrInput
	Value    pulumi.StringInput
}

func (ParameterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*parameterArgs)(nil)).Elem()
}

type ParameterInput interface {
	pulumi.Input

	ToParameterOutput() ParameterOutput
	ToParameterOutputWithContext(ctx context.Context) ParameterOutput
}

func (*Parameter) ElementType() reflect.Type {
	return reflect.TypeOf((**Parameter)(nil)).Elem()
}

func (i *Parameter) ToParameterOutput() ParameterOutput {
	return i.ToParameterOutputWithContext(context.Background())
}

func (i *Parameter) ToParameterOutputWithContext(ctx context.Context) ParameterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ParameterOutput)
}

// ParameterArrayInput is an input type that accepts ParameterArray and ParameterArrayOutput values.
// You can construct a concrete instance of `ParameterArrayInput` via:
//
//	ParameterArray{ ParameterArgs{...} }
type ParameterArrayInput interface {
	pulumi.Input

	ToParameterArrayOutput() ParameterArrayOutput
	ToParameterArrayOutputWithContext(context.Context) ParameterArrayOutput
}

type ParameterArray []ParameterInput

func (ParameterArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Parameter)(nil)).Elem()
}

func (i ParameterArray) ToParameterArrayOutput() ParameterArrayOutput {
	return i.ToParameterArrayOutputWithContext(context.Background())
}

func (i ParameterArray) ToParameterArrayOutputWithContext(ctx context.Context) ParameterArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ParameterArrayOutput)
}

// ParameterMapInput is an input type that accepts ParameterMap and ParameterMapOutput values.
// You can construct a concrete instance of `ParameterMapInput` via:
//
//	ParameterMap{ "key": ParameterArgs{...} }
type ParameterMapInput interface {
	pulumi.Input

	ToParameterMapOutput() ParameterMapOutput
	ToParameterMapOutputWithContext(context.Context) ParameterMapOutput
}

type ParameterMap map[string]ParameterInput

func (ParameterMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Parameter)(nil)).Elem()
}

func (i ParameterMap) ToParameterMapOutput() ParameterMapOutput {
	return i.ToParameterMapOutputWithContext(context.Background())
}

func (i ParameterMap) ToParameterMapOutputWithContext(ctx context.Context) ParameterMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ParameterMapOutput)
}

type ParameterOutput struct{ *pulumi.OutputState }

func (ParameterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Parameter)(nil)).Elem()
}

func (o ParameterOutput) ToParameterOutput() ParameterOutput {
	return o
}

func (o ParameterOutput) ToParameterOutputWithContext(ctx context.Context) ParameterOutput {
	return o
}

// @SUMMARY Foreman representation of parameter. Parameters serve as an identification string that defines autonomy,
// authority, or control for a portion of a network.
func (o ParameterOutput) __meta_() pulumi.BoolOutput {
	return o.ApplyT(func(v *Parameter) pulumi.BoolOutput { return v.__meta_ }).(pulumi.BoolOutput)
}

// ID of the domain to assign this parameter to
func (o ParameterOutput) DomainId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Parameter) pulumi.IntPtrOutput { return v.DomainId }).(pulumi.IntPtrOutput)
}

// ID of the host to assign this parameter to
func (o ParameterOutput) HostId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Parameter) pulumi.IntPtrOutput { return v.HostId }).(pulumi.IntPtrOutput)
}

// ID of the host group to assign this parameter to
func (o ParameterOutput) HostgroupId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Parameter) pulumi.IntPtrOutput { return v.HostgroupId }).(pulumi.IntPtrOutput)
}

func (o ParameterOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Parameter) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// ID of the operating system to assign this parameter to
func (o ParameterOutput) OperatingsystemId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Parameter) pulumi.IntPtrOutput { return v.OperatingsystemId }).(pulumi.IntPtrOutput)
}

// ID of the subnet to assign this parameter to
func (o ParameterOutput) SubnetId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Parameter) pulumi.IntPtrOutput { return v.SubnetId }).(pulumi.IntPtrOutput)
}

func (o ParameterOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v *Parameter) pulumi.StringOutput { return v.Value }).(pulumi.StringOutput)
}

type ParameterArrayOutput struct{ *pulumi.OutputState }

func (ParameterArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Parameter)(nil)).Elem()
}

func (o ParameterArrayOutput) ToParameterArrayOutput() ParameterArrayOutput {
	return o
}

func (o ParameterArrayOutput) ToParameterArrayOutputWithContext(ctx context.Context) ParameterArrayOutput {
	return o
}

func (o ParameterArrayOutput) Index(i pulumi.IntInput) ParameterOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Parameter {
		return vs[0].([]*Parameter)[vs[1].(int)]
	}).(ParameterOutput)
}

type ParameterMapOutput struct{ *pulumi.OutputState }

func (ParameterMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Parameter)(nil)).Elem()
}

func (o ParameterMapOutput) ToParameterMapOutput() ParameterMapOutput {
	return o
}

func (o ParameterMapOutput) ToParameterMapOutputWithContext(ctx context.Context) ParameterMapOutput {
	return o
}

func (o ParameterMapOutput) MapIndex(k pulumi.StringInput) ParameterOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Parameter {
		return vs[0].(map[string]*Parameter)[vs[1].(string)]
	}).(ParameterOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ParameterInput)(nil)).Elem(), &Parameter{})
	pulumi.RegisterInputType(reflect.TypeOf((*ParameterArrayInput)(nil)).Elem(), ParameterArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ParameterMapInput)(nil)).Elem(), ParameterMap{})
	pulumi.RegisterOutputType(ParameterOutput{})
	pulumi.RegisterOutputType(ParameterArrayOutput{})
	pulumi.RegisterOutputType(ParameterMapOutput{})
}
