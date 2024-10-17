%define module	VFSsimple-Drv-Iso

Summary:	A VFSsimple implementation over ISO9660 fs
Name:		perl-%{module}
Version:	0.03
Release:	9
License:	WTFPL
Group:		Development/Perl
URL:		https://nanardon.zarb.org/darcsweb/darcsweb.cgi?r=VFSsimple;a=summary
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBI/%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(URI)
BuildRequires:	perl(Device::Cdio::ISO9660)
BuildRequires:	perl(VFSsimple)
BuildArch:	noarch

%description
This module provide access method for VFSsimple module to access to files
inside ISO9660 CD image.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make CFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.03-6mdv2011.0
+ Revision: 658899
- rebuild for updated spec-helper

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.03-5mdv2010.0
+ Revision: 430649
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.03-4mdv2009.0
+ Revision: 258753
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.03-3mdv2009.0
+ Revision: 246687
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 17 2007 Olivier Thauvin <nanardon@mandriva.org> 0.03-1mdv2008.1
+ Revision: 99452
- initial pkg
- Create perl-VFSsimple-Drv-Iso

