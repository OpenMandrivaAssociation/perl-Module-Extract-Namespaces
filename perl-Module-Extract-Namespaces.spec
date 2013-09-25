%define upstream_name    Module-Extract-Namespaces
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Extract the package declarations from a module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/Module-Extract-Namespaces-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(PPI)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module extracts package declarations from Perl code without running
the code.

It does not extract:

* * packages declared dynamically (e.g. in 'eval')

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 658862
- rebuild for updated spec-helper

* Wed Aug 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 415572
- import perl-Module-Extract-Namespaces


* Wed Aug 12 2009 cpan2dist 0.14-1mdv
- initial mdv release, generated with cpan2dist

