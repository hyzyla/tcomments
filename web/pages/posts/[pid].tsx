import React from 'react';

import { PostPage } from '../../components/PostPage/PostPage';
import { GetServerSideProps, InferGetServerSidePropsType } from "next";
import {getCurrentUser, getPost, getPostComments} from "../../services";


export const getServerSideProps: GetServerSideProps = async (context) => {
    const { params } = context;
    const postID = params.pid;
    // this is client side cookie
    const cookie = context.req ? context.req.headers.cookie : null

    const post = await getPost(postID as string);
    const comments = await getPostComments(postID as string);
    const currentUser = await getCurrentUser(cookie);
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