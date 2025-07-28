        #include <cmrc/cmrc.hpp>
#include <map>
#include <utility>

namespace cmrc {
namespace depthai {

namespace res_chars {
// These are the files which are available in this resource library
// Pointers to /home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/resources/depthai-device-fwp-511fdb6173bbd135949af68a4fbd11de890f8f5e.tar.xz
extern const char* const f_be99_depthai_device_fwp_511fdb6173bbd135949af68a4fbd11de890f8f5e_tar_xz_begin;
extern const char* const f_be99_depthai_device_fwp_511fdb6173bbd135949af68a4fbd11de890f8f5e_tar_xz_end;
// Pointers to /home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/resources/depthai-bootloader-0.0.10.cmd
extern const char* const f_9c53_depthai_bootloader_0_0_10_cmd_begin;
extern const char* const f_9c53_depthai_bootloader_0_0_10_cmd_end;
}

namespace {

const cmrc::detail::index_type&
get_root_index() {
    static cmrc::detail::directory root_directory_;
    static cmrc::detail::file_or_directory root_directory_fod{root_directory_};
    static cmrc::detail::index_type root_index;
    root_index.emplace("", &root_directory_fod);
    struct dir_inl {
        class cmrc::detail::directory& directory;
    };
    dir_inl root_directory_dir{root_directory_};
    (void)root_directory_dir;
    
    root_index.emplace(
        "depthai-device-fwp-511fdb6173bbd135949af68a4fbd11de890f8f5e.tar.xz",
        root_directory_dir.directory.add_file(
            "depthai-device-fwp-511fdb6173bbd135949af68a4fbd11de890f8f5e.tar.xz",
            res_chars::f_be99_depthai_device_fwp_511fdb6173bbd135949af68a4fbd11de890f8f5e_tar_xz_begin,
            res_chars::f_be99_depthai_device_fwp_511fdb6173bbd135949af68a4fbd11de890f8f5e_tar_xz_end
        )
    );
    root_index.emplace(
        "depthai-bootloader-0.0.10.cmd",
        root_directory_dir.directory.add_file(
            "depthai-bootloader-0.0.10.cmd",
            res_chars::f_9c53_depthai_bootloader_0_0_10_cmd_begin,
            res_chars::f_9c53_depthai_bootloader_0_0_10_cmd_end
        )
    );
    return root_index;
}

}

cmrc::embedded_filesystem get_filesystem() {
    static auto& index = get_root_index();
    return cmrc::embedded_filesystem{index};
}

} // depthai
} // cmrc
    