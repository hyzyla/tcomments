import React from 'react';

import { PostPage } from '../../components/PostPage/PostPage';
import { GetServerSideProps, InferGetServerSidePropsType } from "next";
import {getCurrentUser, getPost, getPostComments} from "../../services";


export const getServerSideProps: GetServerSideProps = async (context) => {
    const { params } = context;
    const postID = params.pid;
    const post = await getPost(postID as string);
    const comments = await getPostComments(postID as string);
    const currentUser = await getCurrentUser();
    return {
        props: {
            post,
            comments,
            currentUser,
        }
    }
};


const Pid = ({post, comments, currentUser }: InferGetServerSidePropsType<typeof getServerSideProps>) => {
    return <PostPage post={post} comments={comments} currentUser={currentUser}/>
};


export default Pid;