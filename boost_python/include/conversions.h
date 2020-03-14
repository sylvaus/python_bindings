#pragma once

// based on http://cctbx.sourceforge.net/current_cvs/c_plus_plus/container__conversions_8h-source.html
// docs https://www.boost.org/doc/libs/1_64_0/libs/python/doc/html/reference/to_from_python_type_conversion/boost_python_to_python_converter.html
// https://www.boost.org/doc/libs/1_64_0/libs/python/doc/html/reference/concepts/resultconverter.html
// https://www.boost.org/doc/libs/1_53_0/libs/python/doc/v2/faq.html#custom_string

template<typename VectorType>
struct vector_to_list
{
    using ContainerType = typename std::vector<VectorType>;

    static PyObject *convert(ContainerType const &values)
    {
        boost::python::list result;
        for (const auto& v: values)
        {
            result.append(boost::python::object(v));
        }
        return boost::python::incref(result.ptr());
    }

    static const PyTypeObject *get_pytype()
    { return &PyList_Type; }
};

template<typename VectorType>
void register_vector_to_list() {
    using ContainerType = typename std::vector<VectorType>;
    boost::python::to_python_converter<
        ContainerType,
        vector_to_list<VectorType>
#ifdef BOOST_PYTHON_SUPPORTS_PY_SIGNATURES
        , true
#endif
        >();
}

template<typename VectorType>
struct sequence_to_vector
{
    sequence_to_vector()
    {
        boost::python::converter::registry::push_back(
                &convertible,
                &construct,
                boost::python::type_id<ContainerType>());
    }

    using ContainerType = typename std::vector<VectorType>;
    static void *convertible(PyObject *obj_ptr)
    {
        if (!(PyList_Check(obj_ptr) || PyTuple_Check(obj_ptr)
              || PyIter_Check(obj_ptr) || PyRange_Check(obj_ptr)))
        {
            return 0;
        }
        boost::python::handle<> obj_iter(boost::python::allow_null(PyObject_GetIter(obj_ptr)));
        if (!obj_iter.get())
        { // must be convertible to an iterator
            PyErr_Clear();
            return 0;
        }

        int obj_size = PyObject_Length(obj_ptr);
        if (obj_size < 0)
        { // must be a measurable sequence
            PyErr_Clear();
            return 0;
        }
        for (;;)
        {
            boost::python::handle<> py_elem_hdl(
                    boost::python::allow_null(PyIter_Next(obj_iter.get())));
            if (PyErr_Occurred())
            {
                PyErr_Clear();
                return false;
            }
            if (!py_elem_hdl.get()) break; // end of iteration
            boost::python::object py_elem_obj(py_elem_hdl);
            boost::python::extract<VectorType>
                    elem_proxy(py_elem_obj);
            if (!elem_proxy.check()) return 0;
        }
        return obj_ptr;
    }

    static void construct(
            PyObject *obj_ptr,
            boost::python::converter::rvalue_from_python_stage1_data *data)
    {
        boost::python::handle<> obj_iter(PyObject_GetIter(obj_ptr));
        void *storage = (
                (boost::python::converter::rvalue_from_python_storage<ContainerType> *)
                        data)->storage.bytes;
        new(storage) ContainerType();
        data->convertible = storage;
        ContainerType &result = *((ContainerType *) storage);
        for (;;)
        {
            boost::python::handle<> py_elem_hdl(
                    boost::python::allow_null(PyIter_Next(obj_iter.get())));
            if (PyErr_Occurred()) boost::python::throw_error_already_set();
            if (!py_elem_hdl.get()) break; // end of iteration
            boost::python::object py_elem_obj(py_elem_hdl);
            result.push_back(boost::python::extract<VectorType>(py_elem_obj));
        }
    }
};