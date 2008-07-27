%define version  0.0.1.1
%define release  %mkrel 0.%revision.1
%define revision 838452
%define oname    raptormenu

%define libnamedev %mklibname %{name} -d

Name:		 plasma-applet-%oname
Version:	 %{version}
Release:	 %{release}
License:	 GPLv2+
Url:		 http://www.raptor-menu.org
Group:		 Graphical desktop/KDE
Source0:	 %{oname}-%version.%revision.tar.bz2
Patch0:          raptormenu-0.0.1.1-fix-install.patch
Summary:         Plasmoid Menu for KDE4
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:   cmake >= 2.4.5
BuildRequires:   kdelibs4-devel
BuildRequires:   kdebase4-workspace-devel

%description
Raptor is a plasmoid Menu for KDE4

%files
%defattr(-,root,root)
%{_kde_bindir}/raptormenubin
%{_kde_bindir}/tom-editor
%{_kde_libdir}/raptorplugins/libraptorfancybackground.so
%{_kde_libdir}/kde4/raptormenu_classic.so
%{_kde_libdir}/kde4/raptormenu_nuno.so
%{_kde_appsdir}/raptorapp
%{_kde_appsdir}/desktoptheme/default/raptor-menu/background.svg
%{_kde_appsdir}/desktoptheme/default/raptor-menu/nonaccell.svg
%{_kde_appsdir}/desktoptheme/default/raptor-menu/old.svg
%{_kde_datadir}/kde4/services/classic.desktop
%{_kde_datadir}/kde4/services/raptormenu-nuno.desktop
%{_kde_datadir}/kde4/servicetypes/raptor-backdropplugin.desktop
%{_kde_datadir}/kde4/servicetypes/raptor-dataplugin.desktop
%{_kde_datadir}/kde4/servicetypes/raptor-ui.desktop

#------------------------------------------------

%package        -n     %{libnamedev}
Summary:        Static libraries and headers for %{name}
Group:          Development/C
Provides:       %{name}-devel = %{version}-%{release}

%description  -n     %{libnamedev}
%{libnamedev} contains the libraries and header files needed to
develop programs which make use of %{oname}.

%files -n     %{libnamedev}
%defattr(0644, root, root, 0755)
%{_kde_libdir}/libtom.so
%{_kde_libdir}/libraptorhelper.so
%{_kde_libdir}/libraptormenu.so

#------------------------------------------------

%prep
%setup -q -n %oname
%patch0 -p0

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot
