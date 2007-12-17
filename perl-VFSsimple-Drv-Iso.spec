%define module	VFSsimple-Drv-Iso
%define name	perl-%{module}
%define version	0.03
%define release	%mkrel 1

Summary:	A VFSsimple implementation over ISO9660 fs
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	WTFPL
Group:		Development/Perl
Requires:	perl
URL:		http://nanardon.zarb.org/darcsweb/darcsweb.cgi?r=VFSsimple;a=summary
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBI/%{module}-%{version}.tar.gz
BuildRequires:	perl(URI)
BuildRequires:  perl(Device::Cdio::ISO9660)
BuildRequires:  perl(VFSsimple)
BuildArch: noarch


%description
This module provide access method for VFSsimple module to access to files
inside ISO9660 CD image.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make CFLAGS="%{optflags}"

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/*/*
