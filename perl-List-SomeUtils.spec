#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-SomeUtils
Version  : 0.56
Release  : 16
URL      : https://www.cpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-0.56.tar.gz
Source0  : https://www.cpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-0.56.tar.gz
Summary  : 'Provide the stuff missing in List::Util'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-List-SomeUtils-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(List::SomeUtils::XS)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Try::Tiny)

%description
# NAME
List::SomeUtils - Provide the stuff missing in List::Util
# VERSION
version 0.56

%package dev
Summary: dev components for the perl-List-SomeUtils package.
Group: Development
Provides: perl-List-SomeUtils-devel = %{version}-%{release}

%description dev
dev components for the perl-List-SomeUtils package.


%package license
Summary: license components for the perl-List-SomeUtils package.
Group: Default

%description license
license components for the perl-List-SomeUtils package.


%prep
%setup -q -n List-SomeUtils-0.56

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-SomeUtils
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-List-SomeUtils/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.2/List/SomeUtils.pm
/usr/lib/perl5/vendor_perl/5.28.2/List/SomeUtils/PP.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::SomeUtils.3
/usr/share/man/man3/List::SomeUtils::PP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-SomeUtils/LICENSE
