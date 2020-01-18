Name: pentaho-reporting-flow-engine
Version: 0.9.4
Release: 7%{?dist}
Summary: Pentaho Flow Reporting Engine
License: LGPLv2+
Epoch: 1
Group: System Environment/Libraries
Source: http://downloads.sourceforge.net/jfreereport/flow-engine-%{version}.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant, java-devel, jpackage-utils, libbase, libserializer
BuildRequires: libloader, libfonts, pentaho-libxml, xml-commons-apis
BuildRequires: librepository, sac, flute, liblayout, libformula
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: java, jpackage-utils, libbase >= 1.1.3, libfonts >= 1.1.3
Requires: pentaho-libxml, libformula >= 1.1.3, librepository >= 1.1.3
Requires: sac, flute, liblayout >= 0.2.10, libserializer
BuildArch: noarch

%description
Pentaho Reporting Flow Engine is a free Java report library, formerly
known as 'JFreeReport'

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Documentation
Requires: %{name} = 1:%{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
mkdir -p lib
find . -name "*.jar" -exec rm -f {} \;
build-jar-repository -s -p lib commons-logging-api libbase libloader \
    libfonts libxml jaxp libformula librepository sac flute liblayout \
    libserializer

%build
ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/flow-engine.jar $RPM_BUILD_ROOT%{_javadir}/flow-engine.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Caolán McNamara <caolanm@redhat.com> 1:0.9.4-4
- Related: rhbz#749103 drop gcj aot

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 02 2010 Caolán McNamara <caolanm@redhat.com> 0.9.4-2
- rebuild against libserializer

* Thu Dec 03 2009 Caolán McNamara <caolanm@redhat.com> 0.9.4-1
- latest version

* Fri Jul 24 2009 Caolán McNamara <caolanm@redhat.com> 0.9.2-5.OOo31
- make javadoc no-arch when building as arch-dependant aot

* Sun Mar 29 2009 Caolán McNamara <caolanm@redhat.com> 0.9.2-4.OOo31
- wrong num

* Sat Mar 28 2009 Caolán McNamara <caolanm@redhat.com> 0.9.2-3.OOo31
- tweak version

* Mon Mar 16 2009 Caolán McNamara <caolanm@redhat.com> 0.9.2-1
- OOo tuned version

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 05 2008 Caolán McNamara <caolanm@redhat.com> 0.9.3-2
- wrong liblayout version required

* Wed May 07 2008 Caolán McNamara <caolanm@redhat.com> 0.9.3-1
- initial fedora import
