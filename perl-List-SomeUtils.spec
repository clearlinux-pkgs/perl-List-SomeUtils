#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-List-SomeUtils
Version  : 0.59
Release  : 38
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-0.59.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-0.59.tar.gz
Summary  : 'Provide the stuff missing in List::Util'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-List-SomeUtils-license = %{version}-%{release}
Requires: perl-List-SomeUtils-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(List::SomeUtils::XS)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Try::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
List::SomeUtils - Provide the stuff missing in List::Util
# VERSION
version 0.59

%package dev
Summary: dev components for the perl-List-SomeUtils package.
Group: Development
Provides: perl-List-SomeUtils-devel = %{version}-%{release}
Requires: perl-List-SomeUtils = %{version}-%{release}

%description dev
dev components for the perl-List-SomeUtils package.


%package license
Summary: license components for the perl-List-SomeUtils package.
Group: Default

%description license
license components for the perl-List-SomeUtils package.


%package perl
Summary: perl components for the perl-List-SomeUtils package.
Group: Default
Requires: perl-List-SomeUtils = %{version}-%{release}

%description perl
perl components for the perl-List-SomeUtils package.


%prep
%setup -q -n List-SomeUtils-0.59
cd %{_builddir}/List-SomeUtils-0.59

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-SomeUtils
cp %{_builddir}/List-SomeUtils-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-List-SomeUtils/0146bef281a9daba010a8d641c2ee8e4baef8d22 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::SomeUtils.3
/usr/share/man/man3/List::SomeUtils::PP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-SomeUtils/0146bef281a9daba010a8d641c2ee8e4baef8d22

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
