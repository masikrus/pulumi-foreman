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

type Computeresource struct {
	pulumi.CustomResourceState

	// @SUMMARY Foreman representation of computeresource. ComputeResources serve as an identification string that defines
	// autonomy, authority, or control for a portion of a network.
	__meta_ pulumi.BoolOutput `pulumi:"__meta_"`
	// For VMware only
	Cachingenabled pulumi.BoolPtrOutput `pulumi:"cachingenabled"`
	// For oVirt, VMware Datacenter
	Datacenter pulumi.StringPtrOutput `pulumi:"datacenter"`
	// Description of the compute resource
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
	Displaytype pulumi.StringPtrOutput `pulumi:"displaytype"`
	// The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
	// "Openstack", "Rackspace", "GCE"
	Hypervisor pulumi.StringOutput `pulumi:"hypervisor"`
	// Name of the compute resource
	Name pulumi.StringOutput `pulumi:"name"`
	// Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
	Password pulumi.StringPtrOutput `pulumi:"password"`
	// For VMware
	Server pulumi.StringPtrOutput `pulumi:"server"`
	// For Libvirt and VMware only
	Setconsolepassword pulumi.BoolPtrOutput `pulumi:"setconsolepassword"`
	// URL for Libvirt, oVirt, OpenStack and Rackspace
	Url pulumi.StringOutput `pulumi:"url"`
	// Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
	User pulumi.StringPtrOutput `pulumi:"user"`
}

// NewComputeresource registers a new resource with the given unique name, arguments, and options.
func NewComputeresource(ctx *pulumi.Context,
	name string, args *ComputeresourceArgs, opts ...pulumi.ResourceOption) (*Computeresource, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Hypervisor == nil {
		return nil, errors.New("invalid value for required argument 'Hypervisor'")
	}
	if args.Url == nil {
		return nil, errors.New("invalid value for required argument 'Url'")
	}
	if args.Password != nil {
		args.Password = pulumi.ToSecret(args.Password).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"password",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Computeresource
	err := ctx.RegisterResource("foreman:index/computeresource:Computeresource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetComputeresource gets an existing Computeresource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetComputeresource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ComputeresourceState, opts ...pulumi.ResourceOption) (*Computeresource, error) {
	var resource Computeresource
	err := ctx.ReadResource("foreman:index/computeresource:Computeresource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Computeresource resources.
type computeresourceState struct {
	// @SUMMARY Foreman representation of computeresource. ComputeResources serve as an identification string that defines
	// autonomy, authority, or control for a portion of a network.
	__meta_ *bool `pulumi:"__meta_"`
	// For VMware only
	Cachingenabled *bool `pulumi:"cachingenabled"`
	// For oVirt, VMware Datacenter
	Datacenter *string `pulumi:"datacenter"`
	// Description of the compute resource
	Description *string `pulumi:"description"`
	// For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
	Displaytype *string `pulumi:"displaytype"`
	// The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
	// "Openstack", "Rackspace", "GCE"
	Hypervisor *string `pulumi:"hypervisor"`
	// Name of the compute resource
	Name *string `pulumi:"name"`
	// Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
	Password *string `pulumi:"password"`
	// For VMware
	Server *string `pulumi:"server"`
	// For Libvirt and VMware only
	Setconsolepassword *bool `pulumi:"setconsolepassword"`
	// URL for Libvirt, oVirt, OpenStack and Rackspace
	Url *string `pulumi:"url"`
	// Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
	User *string `pulumi:"user"`
}

type ComputeresourceState struct {
	// @SUMMARY Foreman representation of computeresource. ComputeResources serve as an identification string that defines
	// autonomy, authority, or control for a portion of a network.
	__meta_ pulumi.BoolPtrInput
	// For VMware only
	Cachingenabled pulumi.BoolPtrInput
	// For oVirt, VMware Datacenter
	Datacenter pulumi.StringPtrInput
	// Description of the compute resource
	Description pulumi.StringPtrInput
	// For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
	Displaytype pulumi.StringPtrInput
	// The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
	// "Openstack", "Rackspace", "GCE"
	Hypervisor pulumi.StringPtrInput
	// Name of the compute resource
	Name pulumi.StringPtrInput
	// Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
	Password pulumi.StringPtrInput
	// For VMware
	Server pulumi.StringPtrInput
	// For Libvirt and VMware only
	Setconsolepassword pulumi.BoolPtrInput
	// URL for Libvirt, oVirt, OpenStack and Rackspace
	Url pulumi.StringPtrInput
	// Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
	User pulumi.StringPtrInput
}

func (ComputeresourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*computeresourceState)(nil)).Elem()
}

type computeresourceArgs struct {
	// For VMware only
	Cachingenabled *bool `pulumi:"cachingenabled"`
	// For oVirt, VMware Datacenter
	Datacenter *string `pulumi:"datacenter"`
	// Description of the compute resource
	Description *string `pulumi:"description"`
	// For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
	Displaytype *string `pulumi:"displaytype"`
	// The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
	// "Openstack", "Rackspace", "GCE"
	Hypervisor string `pulumi:"hypervisor"`
	// Name of the compute resource
	Name *string `pulumi:"name"`
	// Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
	Password *string `pulumi:"password"`
	// For VMware
	Server *string `pulumi:"server"`
	// For Libvirt and VMware only
	Setconsolepassword *bool `pulumi:"setconsolepassword"`
	// URL for Libvirt, oVirt, OpenStack and Rackspace
	Url string `pulumi:"url"`
	// Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
	User *string `pulumi:"user"`
}

// The set of arguments for constructing a Computeresource resource.
type ComputeresourceArgs struct {
	// For VMware only
	Cachingenabled pulumi.BoolPtrInput
	// For oVirt, VMware Datacenter
	Datacenter pulumi.StringPtrInput
	// Description of the compute resource
	Description pulumi.StringPtrInput
	// For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
	Displaytype pulumi.StringPtrInput
	// The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
	// "Openstack", "Rackspace", "GCE"
	Hypervisor pulumi.StringInput
	// Name of the compute resource
	Name pulumi.StringPtrInput
	// Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
	Password pulumi.StringPtrInput
	// For VMware
	Server pulumi.StringPtrInput
	// For Libvirt and VMware only
	Setconsolepassword pulumi.BoolPtrInput
	// URL for Libvirt, oVirt, OpenStack and Rackspace
	Url pulumi.StringInput
	// Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
	User pulumi.StringPtrInput
}

func (ComputeresourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*computeresourceArgs)(nil)).Elem()
}

type ComputeresourceInput interface {
	pulumi.Input

	ToComputeresourceOutput() ComputeresourceOutput
	ToComputeresourceOutputWithContext(ctx context.Context) ComputeresourceOutput
}

func (*Computeresource) ElementType() reflect.Type {
	return reflect.TypeOf((**Computeresource)(nil)).Elem()
}

func (i *Computeresource) ToComputeresourceOutput() ComputeresourceOutput {
	return i.ToComputeresourceOutputWithContext(context.Background())
}

func (i *Computeresource) ToComputeresourceOutputWithContext(ctx context.Context) ComputeresourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComputeresourceOutput)
}

// ComputeresourceArrayInput is an input type that accepts ComputeresourceArray and ComputeresourceArrayOutput values.
// You can construct a concrete instance of `ComputeresourceArrayInput` via:
//
//	ComputeresourceArray{ ComputeresourceArgs{...} }
type ComputeresourceArrayInput interface {
	pulumi.Input

	ToComputeresourceArrayOutput() ComputeresourceArrayOutput
	ToComputeresourceArrayOutputWithContext(context.Context) ComputeresourceArrayOutput
}

type ComputeresourceArray []ComputeresourceInput

func (ComputeresourceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Computeresource)(nil)).Elem()
}

func (i ComputeresourceArray) ToComputeresourceArrayOutput() ComputeresourceArrayOutput {
	return i.ToComputeresourceArrayOutputWithContext(context.Background())
}

func (i ComputeresourceArray) ToComputeresourceArrayOutputWithContext(ctx context.Context) ComputeresourceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComputeresourceArrayOutput)
}

// ComputeresourceMapInput is an input type that accepts ComputeresourceMap and ComputeresourceMapOutput values.
// You can construct a concrete instance of `ComputeresourceMapInput` via:
//
//	ComputeresourceMap{ "key": ComputeresourceArgs{...} }
type ComputeresourceMapInput interface {
	pulumi.Input

	ToComputeresourceMapOutput() ComputeresourceMapOutput
	ToComputeresourceMapOutputWithContext(context.Context) ComputeresourceMapOutput
}

type ComputeresourceMap map[string]ComputeresourceInput

func (ComputeresourceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Computeresource)(nil)).Elem()
}

func (i ComputeresourceMap) ToComputeresourceMapOutput() ComputeresourceMapOutput {
	return i.ToComputeresourceMapOutputWithContext(context.Background())
}

func (i ComputeresourceMap) ToComputeresourceMapOutputWithContext(ctx context.Context) ComputeresourceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComputeresourceMapOutput)
}

type ComputeresourceOutput struct{ *pulumi.OutputState }

func (ComputeresourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Computeresource)(nil)).Elem()
}

func (o ComputeresourceOutput) ToComputeresourceOutput() ComputeresourceOutput {
	return o
}

func (o ComputeresourceOutput) ToComputeresourceOutputWithContext(ctx context.Context) ComputeresourceOutput {
	return o
}

// @SUMMARY Foreman representation of computeresource. ComputeResources serve as an identification string that defines
// autonomy, authority, or control for a portion of a network.
func (o ComputeresourceOutput) __meta_() pulumi.BoolOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.BoolOutput { return v.__meta_ }).(pulumi.BoolOutput)
}

// For VMware only
func (o ComputeresourceOutput) Cachingenabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.BoolPtrOutput { return v.Cachingenabled }).(pulumi.BoolPtrOutput)
}

// For oVirt, VMware Datacenter
func (o ComputeresourceOutput) Datacenter() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.StringPtrOutput { return v.Datacenter }).(pulumi.StringPtrOutput)
}

// Description of the compute resource
func (o ComputeresourceOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// For Libvirt: "VNC" or "SPICE". For VMWare: "VNC" or "VMRC"
func (o ComputeresourceOutput) Displaytype() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.StringPtrOutput { return v.Displaytype }).(pulumi.StringPtrOutput)
}

// The HyperVisor/Cloud Provider for this Compute Resource:supported providers include "Libvirt", "Ovirt", "EC2","Vmware",
// "Openstack", "Rackspace", "GCE"
func (o ComputeresourceOutput) Hypervisor() pulumi.StringOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.StringOutput { return v.Hypervisor }).(pulumi.StringOutput)
}

// Name of the compute resource
func (o ComputeresourceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2
func (o ComputeresourceOutput) Password() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.StringPtrOutput { return v.Password }).(pulumi.StringPtrOutput)
}

// For VMware
func (o ComputeresourceOutput) Server() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.StringPtrOutput { return v.Server }).(pulumi.StringPtrOutput)
}

// For Libvirt and VMware only
func (o ComputeresourceOutput) Setconsolepassword() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.BoolPtrOutput { return v.Setconsolepassword }).(pulumi.BoolPtrOutput)
}

// URL for Libvirt, oVirt, OpenStack and Rackspace
func (o ComputeresourceOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.StringOutput { return v.Url }).(pulumi.StringOutput)
}

// Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2.
func (o ComputeresourceOutput) User() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Computeresource) pulumi.StringPtrOutput { return v.User }).(pulumi.StringPtrOutput)
}

type ComputeresourceArrayOutput struct{ *pulumi.OutputState }

func (ComputeresourceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Computeresource)(nil)).Elem()
}

func (o ComputeresourceArrayOutput) ToComputeresourceArrayOutput() ComputeresourceArrayOutput {
	return o
}

func (o ComputeresourceArrayOutput) ToComputeresourceArrayOutputWithContext(ctx context.Context) ComputeresourceArrayOutput {
	return o
}

func (o ComputeresourceArrayOutput) Index(i pulumi.IntInput) ComputeresourceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Computeresource {
		return vs[0].([]*Computeresource)[vs[1].(int)]
	}).(ComputeresourceOutput)
}

type ComputeresourceMapOutput struct{ *pulumi.OutputState }

func (ComputeresourceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Computeresource)(nil)).Elem()
}

func (o ComputeresourceMapOutput) ToComputeresourceMapOutput() ComputeresourceMapOutput {
	return o
}

func (o ComputeresourceMapOutput) ToComputeresourceMapOutputWithContext(ctx context.Context) ComputeresourceMapOutput {
	return o
}

func (o ComputeresourceMapOutput) MapIndex(k pulumi.StringInput) ComputeresourceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Computeresource {
		return vs[0].(map[string]*Computeresource)[vs[1].(string)]
	}).(ComputeresourceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ComputeresourceInput)(nil)).Elem(), &Computeresource{})
	pulumi.RegisterInputType(reflect.TypeOf((*ComputeresourceArrayInput)(nil)).Elem(), ComputeresourceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ComputeresourceMapInput)(nil)).Elem(), ComputeresourceMap{})
	pulumi.RegisterOutputType(ComputeresourceOutput{})
	pulumi.RegisterOutputType(ComputeresourceArrayOutput{})
	pulumi.RegisterOutputType(ComputeresourceMapOutput{})
}
