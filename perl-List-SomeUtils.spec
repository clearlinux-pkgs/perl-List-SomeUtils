#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-SomeUtils
Version  : 0.56
Release  : 6
URL      : https://www.cpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-0.56.tar.gz
Source0  : https://www.cpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-0.56.tar.gz
Summary  : 'Provide the stuff missing in List::Util'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-List-SomeUtils-doc
BuildRequires : perl(List::SomeUtils::XS)
BuildRequires : perl(Module::Implementation)

%description
# NAME
List::SomeUtils - Provide the stuff missing in List::Util
# VERSION
version 0.56

%package doc
Summary: doc components for the perl-List-SomeUtils package.
Group: Documentation

%description doc
doc components for the perl-List-SomeUtils package.


%prep
%setup -q -n List-SomeUtils-0.56

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/List/SomeUtils.pm
/usr/lib/perl5/site_perl/5.26.0/List/SomeUtils/PP.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
