%define version  1.0.0
%define release  %mkrel 0.%revision.5
%define revision 746505
%define oname    raptor

%define libnamedev %mklibname %{name} -d

Name:		 kde4-raptor
Version:	 %{version}
Release:	 %{release}
License:	 GPLv2+
Url:		 http://www.raptor-menu.org
Group:		 Graphical desktop/KDE
Source0:	 %{oname}-%version.%revision.tar.bz2
Summary:         Plasmoid Menu for KDE4
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:   cmake >= 2.4.5
BuildRequires:   kdelibs4-devel
BuildRequires:   kdebase4-workspace-devel

%description
Raptor is a plasmoid Menu for KDE4

%files
%defattr(-,root,root)
%{_kde_bindir}/kandypanel
%{_kde_bindir}/raptorbin
%{_kde_bindir}/tom-editor
%{_kde_libdir}/kde4/raptorlet_apps.so
%{_kde_libdir}/kde4/raptorlet_tom.so
%{_kde_appsdir}/desktoptheme/default/menu/elementbgnormal.svg
%{_kde_appsdir}/desktoptheme/default/menu/raptorslide.svg
%{_kde_appsdir}/kicker/applets/raptor.desktop
%{_kde_datadir}/kde4/services/raptorlet_apps.desktop
%{_kde_datadir}/kde4/services/raptorlet_tom.desktop
%{_kde_datadir}/kde4/servicetypes/raptorlet.desktop


#------------------------------------------------

%define libraptorgui %mklibname raptorgui 1

%package -n %libraptorgui
Summary: Ktorrent core library
Group: System/Libraries

%description -n %libraptorgui
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libraptorgui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libraptorgui -p /sbin/ldconfig
%endif

%files -n %libraptorgui
%defattr(-,root,root)
%{_kde_libdir}/libraptorgui.so.*

#------------------------------------------------

%define libplasmicraptor %mklibname plasmicraptor 1

%package -n %libplasmicraptor
Summary: Ktorrent core library
Group: System/Libraries

%description -n %libplasmicraptor
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libplasmicraptor -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libplasmicraptor -p /sbin/ldconfig
%endif

%files -n %libplasmicraptor
%defattr(-,root,root)
%{_kde_libdir}/libplasmicraptor.so.*

#------------------------------------------------

%package        -n     %{libnamedev}
Summary:        Static libraries and headers for %{name}
Group:          Development/C
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %libplasmicraptor  = %version-%release
Requires:       %libraptorgui = %version-%release

%description  -n     %{libnamedev}
%{libnamedev} contains the libraries and header files needed to
develop programs which make use of %{oname}.

%files -n     %{libnamedev}
%defattr(0644, root, root, 0755)
%{_kde_libdir}/libplasmicraptor.so
%{_kde_libdir}/libraptorgui.so

#------------------------------------------------

%prep
%setup -q -n %oname

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot
